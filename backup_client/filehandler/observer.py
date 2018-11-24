"""Observer Module
"""

import os
import shutil
import datetime
import logging

from watchdog import observers
from watchdog import events
import backup_client.network as gitcom


logger = logging.getLogger(__name__)
loglevel = int(os.getenv('LOG_LEVEL', str(logging.WARNING)))
logging.basicConfig(level=loglevel)

UPDATE_INTERVAL = datetime.timedelta(minutes=0)

class FileObserver(object):

    def __init__(self, username, password):
        self.patterns = {}
        self.file_observer = observers.Observer()
        self.event_handler = events.FileSystemEventHandler()
        self.event_handler.on_modified = self.on_modified
        self.event_handler.on_moved = self.on_moved
        self.credentials = (username, password)

    def add_dir(self, dirname, git_name):
        if os.path.isdir(dirname):
            if not gitcom.is_repo(dirname):
                gitcom.create_new_repo(dirname, git_name, self.credentials)
            else:
                repository = gitcom.find_repo(dirname)
                gitcom.commit_and_push_all(repository, self.credentials)
            self.patterns[dirname] = datetime.datetime.now()
            self.file_observer.schedule(self.event_handler, dirname, recursive=True)

        else:
            print("This is not a folder, You're not suppose to be here")

    def unmonitor_folder(self, repo_name, path):
        #Create some kind of verification that the remote branch has been found and deleted.
        try:
            gitcom.remove_remote_repo(repo_name, self.credentials)
            for watch in self.file_observer._watches: #pylint: disable=W0212
                if watch.path == path:
                    self.file_observer.remove_handler_for_watch(self.event_handler, watch)
                    del self.patterns[path]
                    logger.info("Successfully removed {} from observer.".format(repo_name))
            gitcom.remove_local_repo_data(path)
        except NameError:
            raise
        except BaseException:
            pass

    def start(self):
        self.file_observer.start()

    def stop(self):
        self.file_observer.stop()
        self.file_observer.join()

    def on_modified(self, event):
        mod_path = event.key[1]
        for substring in self.patterns:
            if substring in mod_path and '/.git' not in mod_path:
                logger.info("Modified event: %s", event)
                if datetime.datetime.now() - self.patterns[substring] > UPDATE_INTERVAL:
                    repo = gitcom.find_repo(substring)
                    gitcom.commit_and_push_all(repo, self.credentials)
                    self.patterns[substring] = datetime.datetime.now()
                break

    def on_moved(self, event):
        pass
