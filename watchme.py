import os
import sys
import time
import json
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


BASE_DIR = os.path.realpath(os.path.dirname(sys.argv[0]))

with open(os.path.join(BASE_DIR, "config.json")) as data_file:
    data = json.load(data_file)

SRC_DIR = data["src"]["dir"]
DEST_DIR = data["dest"]["dir"]
SRC_FILE = os.path.join(SRC_DIR, data["src"]["file"])
DEST_FILE = os.path.join(DEST_DIR, data["dest"]["file"])


def copy_resource_to_server(event):
    """Copy SRC_FILE to DEST_FILE"""
    if event.src_path == SRC_FILE:
        shutil.copyfile(SRC_FILE, DEST_FILE)


event_handler = FileSystemEventHandler()

event_handler.on_created = copy_resource_to_server
event_handler.on_modified = copy_resource_to_server

observer = Observer()

observer.schedule(event_handler, SRC_DIR, recursive=False)

observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()

raw_input("")
