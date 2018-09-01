""" Functions for communicating with git server
"""
import time
import os
from json import loads

import pygit2 as git
from pygit2 import clone_repository, RemoteCallbacks, UserPass, Repository, discover_repository  #pylint: disable=E0611
import requests as req

API_CREATE_REPO_URL = 'https://nerobp.xyz/gogs/api/v1/user/repos'
API_GET_USER_DATA = 'https://nerobp.xyz/gogs/api/v1/users/'
GIT_SERVER = 'https://www.nerobp.xyz/gogs/'


def create_new_repository(path, git_name, credentials):
    repo = git.init_repository(path)
    #TODO: Check for subrepositories
    response = req.post(
        API_CREATE_REPO_URL, data={
            'name': git_name,
            'private': True
        }, auth=credentials)
    if response.status_code == 422:
        raise IsADirectoryError({"message":"The repository you are trying to create already exists."})
    clone_url = loads(response.text)['clone_url']
    repo.remotes.set_push_url("origin", clone_url)
    repo.remotes.set_url("origin", clone_url)
    commit_and_push_all(repo, credentials)
    return repo


def add_remote_repository(path, repo_name, credentials):
    clone_url = os.path.join(GIT_SERVER, credentials[0], repo_name)
    if all([credentials[0], credentials[1]]):
        callbacks = RemoteCallbacks(UserPass(credentials[0], credentials[1]))
        return clone_repository(clone_url, path, callbacks=callbacks)

    return clone_repository(clone_url, path)

def pull(repo, credentials, remote_name='origin', branch='master'):
    for remote in repo.remotes:
        if remote.name == remote_name:
            callback = RemoteCallbacks(UserPass(credentials[0], credentials[1]))
            remote.fetch(callbacks=callback)
            remote_master_id = repo.lookup_reference('refs/remotes/origin/%s' % (branch)).target
            merge_result, _ = repo.merge_analysis(remote_master_id)
            # Up to date, do nothing
            if merge_result & git.GIT_MERGE_ANALYSIS_UP_TO_DATE: #pylint: disable=E1101
                return
            # We can just fastforward
            elif merge_result & git.GIT_MERGE_ANALYSIS_FASTFORWARD: #pylint: disable=E1101
                repo.checkout_tree(repo.get(remote_master_id))
                try:
                    master_ref = repo.lookup_reference('refs/heads/%s' % (branch))
                    master_ref.set_target(remote_master_id)
                except KeyError:
                    repo.create_branch(branch, repo.get(remote_master_id))
                repo.head.set_target(remote_master_id)
            elif merge_result & git.GIT_MERGE_ANALYSIS_NORMAL: #pylint: disable=E1101
                repo.merge(remote_master_id)

                if repo.index.conflicts is not None:
                    for conflict in repo.index.conflicts:
                        print('Conflicts found in:', conflict[0].path)
                    raise AssertionError('Conflicts, ahhhhh!!')

                user = repo.default_signature
                tree = repo.index.write_tree()
                commit = repo.create_commit('HEAD',
                                            user,
                                            user,
                                            'Merge!',
                                            tree,
                                            [repo.head.target, remote_master_id])
                # We need to do this or git CLI will think we are still merging.
                repo.state_cleanup()
            else:
                raise AssertionError('Unknown merge analysis result')

def push(repo, credentials=None, remote_name='origin', ref='refs/heads/master:refs/heads/master'):
    if credentials is not None:
        callbacks = RemoteCallbacks(UserPass(credentials[0], credentials[1]))
        for remote in repo.remotes:
            if remote.name == remote_name:
                remote.push([ref], callbacks)
    else:
        for remote in repo.remotes:
            if remote.name == remote_name:
                remote.push([ref])

def is_repo(path):
    repo = discover_repository(path)
    if repo is not None:
        if path in repo:
            return True
    return False


def find_repository(path):
    repo = discover_repository(path)
    if repo is not None:
        if path in repo:
            return Repository(repo)
        return None

def commit_and_push_all(repository, credentials, ref='refs/heads/master'):
    if repository.status():  #pylint: disable=E1101
        repository.index.add_all()
        repository.index.write()

        request = req.get(
            API_GET_USER_DATA + credentials[0],
            auth=credentials)
        if 'full_name' in loads(request.text):
            full_name = loads(request.text)['full_name']
            email = loads(request.text)['email']
        else:
            full_name = "No Name Found"
            email = loads(request.text)['email'] #Email is required for an account so it should never give an error.
        author = git.Signature(full_name, email)  #pylint: disable=E1101
        tree = repository.index.write_tree()

        try:
            repository.create_commit(ref, author, author, \
                                        time.strftime("%d/%m/%Y-%H:%M:%S"), tree, [])
        except BaseException:
            master = repository.lookup_branch('master')
            repository.create_commit(ref, author, author, \
                                        time.strftime("%d/%m/%Y-%H:%M:%S"), tree, [master.target])
        push(repository, credentials)


def get_reponame_from_path(path):
    try:
        repo = Repository(path)
        return os.path.basename(repo.remotes[0].url).replace(".git", "")
    except BaseException:
        return None

def remove_remote_repo(repo_name, credentials):
    response = req.delete(os.path.join('https://nerobp.xyz/gogs/api/v1/repos/', credentials[0], repo_name), auth=credentials)
    if response.status_code == 404:
        raise NameError("Repository not found")
    elif response.status_code != 204:
        raise Exception("Unexpected Error, make sure that you have connection to the server.")

#http://www.pygit2.org/repository.html
#https://github.com/MichaelBoselowitz/pygit2-examples/blob/master/examples.py
