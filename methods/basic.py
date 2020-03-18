"""
copy, move, delete functions
"""
import os
import shutil
from methods import platforms

"""
Tells the user how to insert path according to his OS
"""
def pathPattern():
    if platforms.osType() == "windows":
        print("Path pattern: C:/path/to/file")
    else:
        print("Path pattern: /path/to/file")


"""
Class of basic functions
"""

class Basic():

    """
    Get from the user path to a file and destination.
    Then, copies it from the source to the destination.
    """

    def copy_file(self):
        pathPattern()

        source = input("Insert the source path (including the file): ")
        destination = input("Insert the destination path: ")
        try:
            shutil.copy(str(source), str(destination))
            print("File has been copied to {}".format(str(destination)))
        except:
            print("Couldn't do the operation. Please check your inserted paths.")

    """
    Get from the user path to a folder and destination.
    """

    def copy_folder(self):
        pathPattern()

        source = input("Insert the source path: ")
        destination = input("Insert the destination path: ")
        try:
            shutil.copytree(str(source), str(destination))
            print("Folder has been copied to {}".format(str(destination)))
        except:
            print("Couldn't do the operation. Please check your inserted paths.")

    """
    Can handle folders and files
    """

    def move(self):
        pathPattern()

        source = input("Insert the source path (including the file): ")
        destination = input("Insert the destination path: ")
        try:
            shutil.move(str(source), str(destination))
            print("File has been moved to {}".format(str(destination)))
        except:
            print("Couldn't do the operation. Please check your inserted paths.")

    """
    Gets a file to delete
    """
    
    def delete_file(self):
        pathPattern()

        source = input("Insert the source path (including the file): ")

        if os.path.isfile(str(source)):
            os.remove(str(source))
            print("File has been removed")
        else:
            print("Inserted path is incorrect")

    """
    Deletes a folder
    """

    def delete_folder(self):
        pathPattern()

        source = input("Insert the source path: ")

        if os.path.isdir(str(source)):
            os.rmdir(str(source))
            print("Folder has been removed")
        else:
            print("Inserted path is incorrect")

    def exit(self):
        print("Bye!")
        exit()