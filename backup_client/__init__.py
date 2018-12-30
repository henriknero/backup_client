import os
import datetime
import logging

from backup_client.filehandler import FileObserver
from backup_client.network import GitGogs, is_repo, get_reponame_from_path

logger = logging.getLogger(__name__)


class Backend(FileObserver):
    def __init__(self, config, credentials=None, gitgogs=None):
        super().__init__()
        if gitgogs:
            self.git = gitgogs
        else:
            self.git = GitGogs(config, credentials)

        self.patterns = {}
        self.start()
        self.event_handler.on_modified = self.on_modified

        self._update_interval = datetime.timedelta(minutes=config.UPDATE_INTERVAL)

    def add_dir(self, dir_path, repo_name):
        try:
            self.git.add_dir(dir_path, repo_name)
            self.patterns[dir_path] = datetime.datetime.now()
            self.file_observer.schedule(self.event_handler, dir_path, recursive=True)
        except BaseException as error: #TODO: Add Error Handling for all steps?
            logger.warning("Unable to add directory: %s", error)

    def remove_dir(self, repo_name):
        try:
            dir_path = self.git.get_repo_path(repo_name)
            self.git.remove_remote_repo(repo_name)
            for watch in self.file_observer._watches: #pylint: disable=W0212
                if watch.path == dir_path:
                    self.file_observer.remove_handler_for_watch(self.event_handler, watch)
                    del self.patterns[dir_path]
                    logger.info("Successfully removed %s from observer.", repo_name)
        except NameError:
            raise
        except BaseException:
            pass
    def on_modified(self, event):
        mod_path = event.key[1]
        for substring in self.patterns:
            if substring in mod_path and '/.git' not in mod_path:
                logger.info("Modified event: %s", event)
                if datetime.datetime.now() - self.patterns[substring] > self._update_interval:
                    repo_name = get_reponame_from_path(substring)
                    self.git.commit_and_push_all(repo_name)
                    self.patterns[substring] = datetime.datetime.now()
                break
