import requests as req
import logging
import os

from json import loads
import pygit2 as git

API_CREATE_REPO_URL = 'https://nerobp.xyz/gogs/api/v1/user/repos'
API_GET_USER_DATA = 'https://nerobp.xyz/gogs/api/v1/users/'

logger = logging.getLogger(__name__)
loglevel = int(os.getenv('LOG_LEVEL', str(logging.WARNING)))
logging.basicConfig(level=loglevel)

def remove_remote_repo(repo_name, credentials):
    response = req.delete(os.path.join('https://nerobp.xyz/gogs/api/v1/repos/', credentials[0], repo_name), auth=credentials)
    if response.status_code == 404:
        raise NameError("Repository not found")
    elif response.status_code != 204:
        raise Exception("Unexpected Error, make sure that you have connection to the server.")
    logger.info(" Successfully removed \"{}\" from remote server".format(repo_name))


def create_remote_repo(git_name, credentials):
    response = req.post(
        API_CREATE_REPO_URL, data={
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
        API_GET_USER_DATA + credentials[0],
        auth=credentials)
    if 'full_name' in loads(request.text):
        full_name = loads(request.text)['full_name']
        email = loads(request.text)['email']
    else:
        full_name = "No Name Found"
        email = loads(request.text)['email'] #Email is required for an account so it should not give an error.
    return git.Signature(full_name, email)  #pylint: disable=E1101

def remote_exist(repo_name, credentials):
    httpresponse = req.get(os.path.join("https://nerobp.xyz/gogs/api/v1/repos", credentials[0], repo_name), auth=credentials)
    return not (httpresponse.status_code == 404)

def is_authorized(credentials):
    response = req.get(
        'https://www.nerobp.xyz/gogs/user/login', auth=credentials)
    return response.url == 'https://www.nerobp.xyz/gogs/'
