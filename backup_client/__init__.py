import os
import datetime
import logging

from backup_client.filehandler import FileObserver
from backup_client.network import GitGogs, is_repo

logger = logging.getLogger(__name__)

UPDATE_INTERVAL = datetime.timedelta(minutes=0)

class Backend(FileObserver):
    def __init__(self, api=None, root=None, credentials=None, gitgogs=None):
        super().__init__()
        if gitgogs is None:
            self.git = GitGogs(api, root , credentials)
        else:
            self.git = gitgogs
        self.patterns = {}
        self.start()

    def add_dir(self, dir_path, repo_name):
        try:
            self.git.add_dir(dir_path, repo_name)
            self.patterns[dir_path] = datetime.datetime.now()
            self.file_observer.schedule(self.event_handler, dir_path, recursive=True)
        except BaseException as e: #TODO: Add Error Handling for all steps?
            logger.warning("Unable to add directory: %s" % e)

    def remove_dir(self, repo_name):
        try:
            dir_path = self.git.get_repo_path(repo_name)
            self.git.remove_remote_repo(repo_name)
            for watch in self.file_observer._watches: #pylint: disable=W0212
                if watch.path == dir_path:
                    self.file_observer.remove_handler_for_watch(self.event_handler, watch)
                    del self.patterns[dir_path]
                    logger.info("Successfully removed {} from observer.".format(repo_name))
        except NameError:
            raise
        except BaseException:
            pass