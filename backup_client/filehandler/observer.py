import os

from watchdog import observers
from watchdog import events

class FileObserver(object):
    def __init__(self):
        self.patterns = []
        self.fileobserver = observers.Observer()
        self.event_handler = events.PatternMatchingEventHandler(patterns=self.patterns)
        self.event_handler.on_any_event = self.on_any_event

    def addFile(self,filename):
        if os.path.isfile(filename):
            self.patterns.append(filename)
            self.fileobserver.schedule(self.event_handler, os.path.dirname(filename) ,recursive=False)
            return 0
        else:
            return 1
    def addDir(self,dirname):
        if os.path.isdir(dirname):
            self.fileobserver.schedule(self.event_handler,dirname,recursive=True)
            return 0
        else:
            return 1
    def start(self):
        self.fileobserver.start()
    def stop(self):
        self.fileobserver.stop()
        self.fileobserver.join()
    def on_any_event(self,event):
        print(event)

    

