import logging
import os.path
from json import loads

import requests as req
import pygit2 as git

API = 'https://nerobp.xyz/gogs/api/v1'
ROOT= 'https://nerobp.xyz/gogs'
CREATE = os.path.join(API, 'user/repos')
GET_USER_DATA = os.path.join(API, 'users')
GET_DELETE = os.path.join(API, 'repos')
LOGIN = os.path.join(ROOT, 'user/login')

logger = logging.getLogger(__name__)

def remove_remote_repo(repo_name, credentials):
    response = req.delete(os.path.join(GET_DELETE, credentials[0], repo_name), auth=credentials)
    if response.status_code == 404:
        raise NameError("Repository not found")
    elif response.status_code != 204:
        raise Exception("Unexpected Error, make sure that you have connection to the server.")
    logger.info(" Successfully removed \"{}\" from remote server".format(repo_name))


def create_remote_repo(git_name, credentials):
    response = req.post(
        CREATE, data={
            'name': git_name,
            'private': True
        },
        auth=credentials)
    if response.status_code == 422:
        raise IsADirectoryError({"message":"The repository you are trying to create already exists."})
    try:
        return loads(response.text)['clone_url']
    except:
        pass #TODO: Error Handling


def get_signature(credentials):
    request = req.get(
        GET_USER_DATA + credentials[0],
        auth=credentials)
    if 'full_name' in loads(request.text):
        full_name = loads(request.text)['full_name']
        email = loads(request.text)['email']
    else:
        full_name = "No Name Found"
        email = loads(request.text)['email'] #Email is required for an account so it should not give an error.
    return git.Signature(full_name, email)  #pylint: disable=E1101

def remote_exist(repo_name, credentials):
    httpresponse = req.get(os.path.join(GET_DELETE, credentials[0], repo_name), auth=credentials)
    return not (httpresponse.status_code == 404)

def is_authorized(credentials):
    response = req.get(
        LOGIN, auth=credentials)
    return response.url == ROOT
