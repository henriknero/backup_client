import logging
import os.path
from json import loads

import requests as req
import pygit2 as git

logger = logging.getLogger(__name__)

class GitApi(object):
    def __init__(self, api, credentials=None, root=None):
        self.api = api
        self.credentials = credentials
        if root:
            self.root = root
        else:
            self.root = api[:api.find('api')]
        self.create = os.path.join(self.api, 'user/repos')
        self.get_user_data = os.path.join(self.api, 'users')
        self.get_delete = os.path.join(self.api, 'repos')
        self.login = os.path.join(self.root, 'user/login')

    def remove_remote_repo(self, repo_name):
        response = req.delete(os.path.join(self.get_delete, self.credentials[0], repo_name), auth=self.credentials)
        if response.status_code == 404:
            raise NameError("Repository not found")
        elif response.status_code != 204:
            raise Exception("Unexpected Error, make sure that you have connection to the server.")
        logger.info(" Successfully removed \"%s\" from remote server", repo_name)


    def create_remote_repo(self, git_name):
        response = req.post(
            self.create, data={
                'name': git_name,
                'private': True
            },
            auth=self.credentials)
        if response.status_code == 422:
            raise IsADirectoryError({"message":"The repository you are trying to create already exists."})
        try:
            return loads(response.text)['clone_url']
        except:
            pass #TODO: Error Handling


    def get_signature(self):
        request = req.get(
            os.path.join(self.get_user_data, self.credentials[0]),
            auth=self.credentials)
        if 'full_name' in loads(request.text):
            full_name = loads(request.text)['full_name']
            email = loads(request.text)['email']
        else:
            full_name = "No Name Found"
            email = loads(request.text)['email'] #Email is required for an account so it should not give an error.
        return git.Signature(full_name, email)  #pylint: disable=E1101

    def remote_exist(self, repo_name):
        httpresponse = req.get(os.path.join(self.get_delete, self.credentials[0], repo_name), auth=self.credentials)
        return not httpresponse.status_code == 404

    def is_authorized(self):
        response = req.get(
            self.login, auth=self.credentials)
        return response.url == self.root
