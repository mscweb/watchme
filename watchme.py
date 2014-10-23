import os
import sys
import time
import json
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def read_config_file(filename):
    BASE_DIR = os.path.realpath(os.path.dirname(sys.argv[0]))

    with open(os.path.join(BASE_DIR, filename)) as data_file:
        data = json.load(data_file)

    return data


def copy_resource_to_server(event):
    """Copy source file to destination"""
    data = read_config_file("config.json")

    src_file = os.path.join(data["src"]["dir"], data["src"]["file"])
    dest_file = os.path.join(data["dest"]["dir"], data["dest"]["file"])

    if event.src_path == src_file:
        shutil.copyfile(src_file, dest_file)


def _main():
    event_handler = FileSystemEventHandler()

    event_handler.on_created = copy_resource_to_server
    event_handler.on_modified = copy_resource_to_server

    observer = Observer()

    data = read_config_file("config.json")
    observer.schedule(event_handler, data["src"]["dir"], recursive=False)

    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

    raw_input("")


if __name__ == "__main__":
    _main()
