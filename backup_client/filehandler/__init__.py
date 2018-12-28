from watchdog import observers
from watchdog import events
import backup_client.network as gitcom


class FileObserver(object):

    def __init__(self):
        self.file_observer = observers.Observer()
        self.event_handler = events.FileSystemEventHandler()


    def start(self):
        self.file_observer.start()

    def stop(self):
        self.file_observer.stop()
        self.file_observer.join()


