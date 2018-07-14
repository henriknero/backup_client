"""Observer Module
"""

import os

from watchdog import observers
from watchdog import events
from backup_client.network import gitcom
import pygit2


class FileObserver(object):
    """Observer Class
    """

    def __init__(self):
        self.patterns = []
        self.file_observer = observers.Observer()
        self.event_handler = events.FileSystemEventHandler()
        self.event_handler.on_any_event = self.on_any_event

    def add_file(self, filename):
        """Add file function

        Arguments:
            filename {string} -- path to file that is to be observed
        """

        if os.path.isfile(filename):
            self.patterns.append(filename)
            self.file_observer.schedule(
            self.event_handler, os.path.dirname(filename), recursive=False)
        else:
            print("This file does not exist")

    def add_dir(self, dirname):
        """Add dir function

        Arguments:
            dirname {string} -- Path to dir that is to be observed recursively
        """

        if os.path.isdir(dirname):
            self.patterns.append(dirname)
            self.file_observer.schedule(self.event_handler, dirname, recursive=True)
            repo = gitcom.add_local_repository(dirname)
            if repo is not None:
                gitcom.commit_and_push_all(repo)
            #TODO Remove files that are selected but lie under this. For efficiency reasons
        else:
            print("This is not a folder")

    def start(self):
        """Start
        """

        self.file_observer.start()

    def stop(self):
        """Stop
        """

        self.file_observer.stop()
        self.file_observer.join()

    def on_any_event(self, event):
        """Event handling Function

        Arguments:
            event {event} -- Contains information about changes done to file
        """

        if any(substring in event.key[1] for substring in self.patterns):
            print(event)
