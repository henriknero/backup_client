import time
import datetime
import os
import shutil
import logging
from json import loads
from pygit2 import Repository, discover_repository, init_repository  #pylint: disable=E0611
import requests as req

from .git import GitClient
from .gogs import GitApi

logger = logging.getLogger(__name__)

UPDATE_INTERVAL = datetime.timedelta(minutes=0)
class GitGogs():
    def __init__(self, config, credentials):
        self.api = GitApi(config.API, credentials)
        self.root = config.ROOT
        self.repos = {}

    def add_dir(self, dir_path, repo_name):
        if os.path.isdir(dir_path):
            if is_repo(dir_path):
                self.create_existing_repo(dir_path, repo_name)
            else:
                self.create_new_repo(dir_path, repo_name)


    def remove_remote_repo(self, repo_name):
        repo_path = self.repos[repo_name].path
        remove_local_repo_data(repo_path)
        self.api.remove_remote_repo(repo_name)
        del self.repos[repo_name]
    def create_new_repo(self, path, git_name):
        try:
            repo = GitClient(self.api.get_signature(), path, self.root, credentials = self.api.credentials).init()
            try:
                clone_url = self.api.create_remote_repo(git_name)
                repo.repo.remotes.set_push_url("origin", clone_url)
                repo.repo.remotes.set_url("origin", clone_url)
                self.repos[git_name] = repo
                self.commit_and_push_all(git_name)
                return repo
            except:
                self.api.remove_remote_repo(git_name)
                raise
        except BaseException as e:
            remove_local_repo_data(path)
            logger.warning("Unable to create repository %s in %s because of %s" % (git_name, path, e))

    def create_existing_repo(self, path, git_name):
        try:
            repo = GitClient(self.api.get_signature(), path, self.root, credentials=self.api.credentials).find()
            self.repos[git_name] = repo
            self.commit_and_push_all(git_name)
        except BaseException as e:
            logger.warning("Unable to create repository %s in %s because of %s" % (git_name, path, e))
    def add_remote_repo(self, path, repo_name):
        return self.repos[repo_name].clone(path, repo_name, self.api.credentials)

    def commit_and_push_all(self, repo_name):
        self.repos[repo_name].add_all()
        self.repos[repo_name].commit(time.strftime("%d/%m/%Y-%H:%M:%S"))
        self.repos[repo_name].push()

    def update_remote(self,repo_name):
        self.repos[repo_name].pull()
        self.commit_and_push_all(repo_name)
    
    def verify_remote(self, path ,repo_name):
        repo = Repository(path)
        response = []
        if not repo_name in os.path.basename(repo.remotes[0].url):
            response.append(1)
        if not self.api.remote_exist(repo_name):
            response.append(2)
        return response
    def get_repo_path(self, repo_name):
        return self.repos[repo_name].path

def get_reponame_from_path(path):
    try:
        repo = Repository(path)
        return os.path.basename(repo.remotes[0].url).replace(".git", "")
    except BaseException:
        return None

def remove_local_repo_data(path):
    shutil.rmtree(os.path.join(path, ".git"))
    logger.info(" Successfully removed .git in {}".format(path))


def is_repo(path):
    try:
        repo = discover_repository(path)
        if repo is not None:
            if path in repo:
                return True
        return False
    except KeyError:
        return False



#http://www.pygit2.org/repository.html
#https://github.com/MichaelBoselowitz/pygit2-examples/blob/master/examples.py
