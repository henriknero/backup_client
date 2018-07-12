import os

from watchdog import observers
from watchdog import events


class FileObserver(object):
    def __init__(self):
        self.patterns = []
        self.file_observer = observers.Observer()
        self.event_handler = events.FileSystemEventHandler()
        self.event_handler.on_any_event = self.on_any_event

    def add_file(self, filename):
        if os.path.isfile(filename):
            self.patterns.append(filename)
            self.file_observer.schedule(self.event_handler, os.path.dirname(filename), recursive=False)
        else:
            print("This file does not exist")

    def add_dir(self, dirname):
        if os.path.isdir(dirname):
            self.patterns.append(dirname)
            self.file_observer.schedule(self.event_handler, dirname, recursive=True)
            #TODO Remove files that are selected but lie under this.
        else:
            print("This is not a folder")

    def start(self):
        self.file_observer.start()

    def stop(self):
        self.file_observer.stop()
        self.file_observer.join()

    def on_any_event(self, event):
        if any(substring in event.key[1] for substring in self.patterns):
            print(event)
