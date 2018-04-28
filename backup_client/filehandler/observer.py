from watchdog import observers
from watchdog import events

class FileObserver(object):
    def __init__(self):
        self.patterns = []
        self.fileobserver = observers.Observer()
        self.event_handler = events.PatternMatchingEventHandler(patterns=self.patterns)
        self.event_handler.on_any_event = self.on_any_event

    def addFile(self,filename):
        self.patterns.append(filename)
        self.fileobserver.schedule(self.event_handler,'.',recursive=False)
    def addDir(self,dirname):
        self.fileobserver.schedule(self.event_handler,dirname,recursive=True)
    def start(self):
        self.fileobserver.start()
    def stop(self):
        self.fileobserver.stop()
        self.fileobserver.join()
    def on_any_event(self,event):
        print(event)

    

