import os
import logging


import pygit2 as git
from pygit2 import RemoteCallbacks, UserPass, clone_repository, init_repository, discover_repository #pylint: disable=E0611

logger = logging.getLogger(__name__)

class GitClient(object):
    def __init__(self, signature, path, server, credentials=None, remote_name='origin', ref='refs/heads/master'):
        self.repo = None
        self.credentials = credentials
        self.remote_name = remote_name
        self.ref = ref
        self.signature = signature
        self.path = path
        self.server = server

    def push(self):
        if self.credentials is not None:
            callbacks = RemoteCallbacks(UserPass(self.credentials[0], self.credentials[1]))
            for remote in self.repo.remotes:
                if remote.name == self.remote_name:
                    remote.push([self.ref], callbacks)
        else:
            for remote in self.repo.remotes:
                if remote.name == self.remote_name:
                    remote.push([self.ref])
        logger.info("Push done at: %s", self.repo.path)

    def pull(self, branch='master'):
        for remote in self.repo.remotes:
            if remote.name == self.remote_name:
                callback = RemoteCallbacks(UserPass(self.credentials[0], self.credentials[1]))
                remote.fetch(callbacks=callback)
                remote_master_id = self.repo.lookup_reference('FETCH_HEAD').target
                merge_result, _ = self.repo.merge_analysis(remote_master_id)
                # Up to date, do nothing
                if merge_result & git.GIT_MERGE_ANALYSIS_UP_TO_DATE: #pylint: disable=E1101
                    return
                # We can just fastforward
                elif merge_result & git.GIT_MERGE_ANALYSIS_FASTFORWARD: #pylint: disable=E1101
                    self.repo.checkout_tree(self.repo.get(remote_master_id))
                    try:
                        master_ref = self.repo.lookup_reference('refs/heads/%s' % (branch))
                        master_ref.set_target(remote_master_id)
                    except KeyError:
                        self.repo.create_branch(branch, self.repo.get(remote_master_id))
                    self.repo.head.set_target(remote_master_id)
                elif merge_result & git.GIT_MERGE_ANALYSIS_NORMAL: #pylint: disable=E1101
                    self.repo.merge(remote_master_id)

                    if self.repo.index.conflicts is not None:
                        for conflict in self.repo.index.conflicts:
                            print('Conflicts found in:', conflict[0].path)
                        raise AssertionError('Conflicts, ahhhhh!!')

                    tree = self.repo.index.write_tree()
                    self.repo.create_commit('HEAD',
                                            self.signature,
                                            self.signature,
                                            'Merge!',
                                            tree,
                                            [self.repo.head.target, remote_master_id])
                    # We need to do this or git CLI will think we are still merging.
                    self.repo.state_cleanup()
                else:
                    raise AssertionError('Unknown merge analysis result')
        logger.info("Pull request done on: %s", self.repo.path)

    def add_all(self):
        for filename in self.repo.status():
            if filename[-1] != '/':
                if os.path.exists(os.path.join(self.repo.workdir, filename)):
                    self.repo.index.add(filename)
                else:
                    self.repo.index.remove(filename)
            else:
                self.repo.index.add(filename[:-1])

    def commit(self, message):
        self.repo.index.write()
        tree = self.repo.index.write_tree()
        try:
            self.repo.create_commit(self.ref, self.signature, self.signature, message, tree, [])
        except BaseException:
            master = self.repo.lookup_branch('master')
            self.repo.create_commit(self.ref, self.signature, self.signature, message, tree, [master.target])

    def clone(self, repo_name):
        clone_url = os.path.join(self.server, repo_name, self.credentials[0])
        callbacks = RemoteCallbacks(UserPass(self.credentials[0], self.credentials[1]))
        return clone_repository(clone_url, self.path, callbacks=callbacks)

    def init(self):
        self.repo = init_repository(self.path)
        return self
    def find(self):
        repo = discover_repository(self.path)
        if repo is not None:
            if self.path in repo:
                self.repo = git.Repository(repo)
                return self
            return None
