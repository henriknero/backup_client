""" Functions for communicating with git server
"""
import time

import pygit2 as git
from pygit2 import clone_repository, RemoteCallbacks, UserPass, Repository, discover_repository #pylint: disable=E0611

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
    else:
        return clone_repository(url, path)

def add_local_repository(path):
    return Repository(path)

def find_repository(path):
    repo = discover_repository(path)
    if repo is not None:
        return Repository(repo)
def commit_and_push_all(repository):
    if any(value > 0 for value in repository.status().values()): #pylint: disable=E1101
        repository.index.add_all()
        repository.index.write()
        ref = "refs/heads/master"
        author = git.Signature("Henrik Nero", "henriknero@gmail.com") #pylint: disable=E1101
        tree = repository.index.write_tree()
        master = repository.lookup_branch('master')
        commit = repository.create_commit(ref, author, author, time.strftime("%d/%m/%Y"), tree, [master.target])

#http://www.pygit2.org/repository.html
git.Branch.target