""" Functions for communicating with git server
"""
import time
from json import loads

import pygit2 as git
from pygit2 import clone_repository, RemoteCallbacks, UserPass, Repository, discover_repository  #pylint: disable=E0611
import requests as req

API_URL = 'https://nerobp.xyz/gogs/api/v1/user/repos'


def create_new_repository(path, credentials):
    repo = git.init_repository(path)
    repo_name = path.replace('/', '_')
    response = req.post(
        API_URL, data={
            'name': repo_name,
            'private': True
        }, auth=credentials)
    if response.status_code == 422:
        print("This repo already exists, you should not be here")
        return
    clone_url = loads(response.text)['clone_url']
    repo.remotes.set_push_url("origin", clone_url)

    commit_and_push_all(repo, credentials)


def add_remote_repository(url, path, username=None, password=None):
    """Download a existing repository to path

    Arguments:
        url {string} -- url to Download repo from
        path {string} -- Path to download repo to

    Keyword Arguments:
        bare {bool} -- [description] (default: {False})
    """
    if all([username, password]):
        callbacks = RemoteCallbacks(UserPass(username, password))
        return clone_repository(url, path, callbacks=callbacks)

    return clone_repository(url, path)


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
    else:
        return None


def commit_and_push_all(repository, credentials):
    if repository.status():  #pylint: disable=E1101
        repository.index.add_all()
        repository.index.write()
        ref = "refs/heads/master"
        request = req.get(
            'https://nerobp.xyz/gogs/api/v1/users/' + credentials[0],
            auth=credentials)
        full_name = loads(request.text)['full_name']
        email = loads(request.text)['email']
        author = git.Signature(full_name, email)  #pylint: disable=E1101
        tree = repository.index.write_tree()
        try:
            repository.create_commit(ref, author, author, \
                                        time.strftime("%d/%m/%Y-%H:%M:%S"), tree, [])
        except BaseException:
            master = repository.lookup_branch('master')
            repository.create_commit(ref, author, author, \
                                        time.strftime("%d/%m/%Y-%H:%M:%S"), tree, [master.target])

        repository.remotes[0].push([ref],
                                   RemoteCallbacks(
                                       UserPass(credentials[0],
                                                credentials[1])))


#http://www.pygit2.org/repository.html
