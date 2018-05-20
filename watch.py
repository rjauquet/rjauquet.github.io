import sys
import time
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from build import build

class BuildEventHandler(FileSystemEventHandler):

    locked = False
    files_changed_while_locked = 0

    def on_modified(self, event):
        if not self.locked:
            print('building project...')
            build()
            print(f'Done! {self.files_changed_while_locked} files changed while building')
            self.files_changed_while_locked = 0
            self.locked = False
        else:
            self.files_changed_while_locked += 1

if __name__ == "__main__":
    path = './content/'
    event_handler = BuildEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
