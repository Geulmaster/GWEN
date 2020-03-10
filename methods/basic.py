"""
copy, move, delete functions
"""
import os
import shutil
from methods import platforms

class Basic():
    
    def copy_file(self):
        if platforms.osType() == "windows":
            print("Path pattern: C:/path/to/file")
        else:
            print("Path pattern: /path/to/file")

        source = input("Insert the source path (including the file): ")
        destination = input("Insert the destination path: ")

        shutil.copy(str(source), str(destination))
        print("File was copied to {}".format(str(destination)))


    def yo(self):
        print("yoy")