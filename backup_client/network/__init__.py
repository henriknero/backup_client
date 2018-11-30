import time
import os
import shutil
import logging
from json import loads

from pygit2 import Repository, discover_repository, init_repository  #pylint: disable=E0611

from .git import push, pull, add_all, commit, clone, init
import requests as req
from .gogs import create_remote_repo, remove_remote_repo, get_signature, remote_exist

logger = logging.getLogger(__name__)
loglevel = int(os.getenv('LOG_LEVEL', str(logging.WARNING)))
logging.basicConfig(level=loglevel)



def create_new_repo(path, git_name, credentials):
    try:
        repo = init(path)
        try:
            clone_url = create_remote_repo(git_name, credentials)
            repo.remotes.set_push_url("origin", clone_url)
            repo.remotes.set_url("origin", clone_url)
            commit_and_push_all(repo, credentials)
            return repo
        except:
            remove_remote_repo(git_name, credentials)
            raise
    except BaseException as e:
        remove_local_repo_data(path)
        logger.warning("Unable to create repository {} in {} because of {}".format(git_name, path, e))

def add_remote_repo(path, repo_name, credentials):
    return clone(path, repo_name, credentials)

def is_repo(path):
    repo = discover_repository(path)
    if repo is not None:
        if path in repo:
            return True
    return False

def find_repo(path):
    repo = discover_repository(path)
    if repo is not None:
        if path in repo:
            return Repository(repo)
        return None

def commit_and_push_all(repository, credentials, ref='refs/heads/master'):
    add_all(repository)
    commit(repository, credentials, get_signature(credentials), time.strftime("%d/%m/%Y-%H:%M:%S"), ref)
    push(repository, credentials)


def get_reponame_from_path(path):
    try:
        repo = Repository(path)
        return os.path.basename(repo.remotes[0].url).replace(".git", "")
    except BaseException:
        return None

def remove_local_repo_data(path):
    shutil.rmtree(os.path.join(path, ".git"))
    logger.info(" Successfully removed .git in {}".format(path))

def update_remote(path, credentials):
    repo = find_repo(path)
    pull(repo, credentials, get_signature(credentials))
    commit_and_push_all(repo, credentials)
def verify_remote(path, repo_name, credentials):
    repo = find_repo(path)
    response = []
    if not repo_name in os.path.basename(repo.remotes[0].url):
        response.append(1)
    if not remote_exist(repo_name, credentials):
        response.append(2)
    return response


#http://www.pygit2.org/repository.html
#https://github.com/MichaelBoselowitz/pygit2-examples/blob/master/examples.py
