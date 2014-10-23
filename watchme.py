import os
import sys
import time
import json
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def read_config_file(filename):
    try:
        BASE_DIR = os.path.realpath(os.path.dirname(sys.argv[0]))

        with open(os.path.join(BASE_DIR, filename)) as data_file:
            data = json.load(data_file)

        return data
    except Exception as ex:
        print type(ex)     # the exception instance
        print ex
        print "Error in reading the config file"
        return "[]"


def copy_resource_to_server(event):
    try:
        data = read_config_file("config.json")
        src_file = os.path.join(data["src"]["dir"], data["src"]["file"])
        dest_file = os.path.join(data["dest"]["dir"], data["dest"]["file"])
        #If destination directory does not exist, create it
        if not os.path.exists(data["dest"]["dir"]):
            os.makedirs(data["dest"]["dir"])
        if event.src_path == src_file:
            """Copy source file to destination"""
            shutil.copyfile(src_file, dest_file)
    except Exception as ex:
        print type(ex)     # the exception instance
        print ex
        print "Error in copying resource to server"

def _main():
    try:
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
    except Exception as ex:
        print type(ex)     # the exception instance
        print ex
        print "Error in main"



if __name__ == "__main__":
    _main()
