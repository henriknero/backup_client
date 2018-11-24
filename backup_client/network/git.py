import os
import logging


import pygit2 as git
from pygit2 import RemoteCallbacks, UserPass, clone_repository, init_repository


logger = logging.getLogger(__name__)
loglevel = int(os.getenv('LOG_LEVEL', str(logging.WARNING)))
logging.basicConfig(level=loglevel)

GIT_SERVER = 'https://www.nerobp.xyz/gogs/'

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
    logger.info("Push done at: %s", repo.path)

def pull(repo, credentials, signature, remote_name='origin', branch='master'):
    for remote in repo.remotes:
        if remote.name == remote_name:
            callback = RemoteCallbacks(UserPass(credentials[0], credentials[1]))
            remote.fetch(callbacks=callback)
            remote_master_id = repo.lookup_reference('FETCH_HEAD').target
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

                tree = repo.index.write_tree()
                repo.create_commit('HEAD',
                                   signature,
                                   signature,
                                   'Merge!',
                                   tree,
                                   [repo.head.target, remote_master_id])
                # We need to do this or git CLI will think we are still merging.
                repo.state_cleanup()
            else:
                raise AssertionError('Unknown merge analysis result')
    logger.info("Pull request done on: %s", repo.path)

def add_all(repository):
    for filename in repository.status():
        if filename[-1] != '/':
            if os.path.exists(os.path.join(repository.workdir, filename)):
                repository.index.add(filename)
            else:
                repository.index.remove(filename)
        else:
            repository.index.add(filename[:-1])

def commit(repository, credentials, author, message, ref='refs/heads/master'):
    repository.index.write()
    tree = repository.index.write_tree()
    try:
        repository.create_commit(ref, author, author, message, tree, [])
    except BaseException:
        master = repository.lookup_branch('master')
        repository.create_commit(ref, author, author, message, tree, [master.target])
def clone(path, repo_name, credentials):
    clone_url = os.path.join(GIT_SERVER, credentials[0], repo_name)
    callbacks = RemoteCallbacks(UserPass(credentials[0], credentials[1]))
    return clone_repository(clone_url, path, callbacks=callbacks)

def init(path):
    return init_repository(path)