import os

from watchdog import observers
from watchdog import events


class FileObserver(object):
    def __init__(self):
        self.patterns = []
        self.file_observer = observers.Observer()
        self.event_handler = events.PatternMatchingEventHandler(patterns=self.patterns)
        self.event_handler.on_any_event = self.on_any_event

    def add_file(self, filename):
        if os.path.isfile(filename):
            self.patterns.append(filename)
            self.file_observer.schedule(self.event_handler, os.path.dirname(filename), recursive=False)
            return 0
        else:
            return 1

    def add_dir(self, dirname):
        if os.path.isdir(dirname):
            self.file_observer.schedule(self.event_handler, dirname, recursive=True)
            return 0
        else:
            return 1

    def start(self):
        self.file_observer.start()

    def stop(self):
        self.file_observer.stop()
        self.file_observer.join()

    @staticmethod
    def on_any_event(event):
        print(event)
