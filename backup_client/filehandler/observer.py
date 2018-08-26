"""Observer Module
"""

import os
import shutil
import datetime

from watchdog import observers
from watchdog import events
from backup_client.network import gitcom

UPDATE_INTERVAL = datetime.timedelta(minutes=0)

class FileObserver(object):
    """Observer Class
    """

    def __init__(self, username, password):
        self.patterns = {}
        self.file_observer = observers.Observer()
        self.event_handler = events.FileSystemEventHandler()
        self.event_handler.on_modified = self.on_modified
        self.event_handler.on_moved = self.on_moved
        self.credentials = (username, password)

    def add_dir(self, dirname, git_name):
        """Add dir function

        Arguments:
            dirname {string} -- Path to dir that is to be observed recursively
        """

        if os.path.isdir(dirname):
            if not gitcom.is_repo(dirname):
                gitcom.create_new_repository(dirname, git_name, self.credentials)
            else:
                repository = gitcom.find_repository(dirname)
                gitcom.commit_and_push_all(repository, self.credentials)
            
            self.patterns[dirname] = datetime.datetime.now()
            self.file_observer.schedule(self.event_handler, dirname, recursive=True)

        else:
            print("This is not a folder, You're not suppose to be here")

    def unmonitor_folder(self, repo_name, path):
        #Create some kind of verification that the remote branch has been found and deleted.
        try:
            gitcom.remove_remote_repo(repo_name, self.credentials)
            for watch in self.file_observer._watches:
                if watch.path == path:
                    self.file_observer.remove_handler_for_watch(self.event_handler, watch)
            shutil.rmtree(os.path.join(path, ".git"))
        except NameError:
            raise
        except BaseException:
            pass

    def start(self):
        """Start
        """
        self.file_observer.start()

    def stop(self):
        """Stop
        """
        self.file_observer.stop()
        self.file_observer.join()

    def on_modified(self, event):
        """Event handling Function

        Arguments:
            event {event} -- Contains information about changes done to file
        """
        mod_path = event.key[1]
        for substring in self.patterns:
            if substring in mod_path and '/.git' not in mod_path:
                if datetime.datetime.now() - self.patterns[substring] > UPDATE_INTERVAL:
                    repo = gitcom.find_repository(substring)
                    gitcom.commit_and_push_all(repo, self.credentials)
                    self.patterns[substring] = datetime.datetime.now()
                break

    def on_moved(self, event):
        """Event handling Function

        Arguments:
            event {event} -- Contains information about changes done to file
        """
        pass
        #TODO Make this function...

    # def add_file(self, filename):
    #     """Add file function

    #     Arguments:
    #         filename {string} -- path to file that is to be observed
    #     """

    #     if os.path.isfile(filename):
    #         self.patterns[filename] = 0
    #         self.file_observer.schedule(
    #         self.event_handler, os.path.dirname(filename), recursive=False)
    #     else:
    #         print("This file does not exist")
