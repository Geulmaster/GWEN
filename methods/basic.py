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
    Gets from the user the extension of files and copies all of them.
    """

    def copy_multiple(self):
        pathPattern()

        source = input("Insert the source path: ")
        extension = input("Insert the files extension: ")
        destination = input("Insert the destination path: ")

        for file_name in os.listdir(source):
            if file_name.endswith(str(extension)):
                pathname = os.path.join(source, file_name)
                if os.path.isfile(pathname):
                    shutil.copy2(pathname, destination)

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

    """
    Gets from the user the extension of files and deletes all of them.
    """

    def delete_multiple(self):
        pathPattern()

        source = input("Insert the source path: ")
        extension = input("Insert the files extension: ")
        destination = input("Insert the destination path: ")

        for file_name in os.listdir(source):
            if file_name.endswith(str(extension)):
                pathname = os.path.join(source, file_name)
                if os.path.isfile(pathname):
                    os.remove(str(pathname))

    def exit(self):
        print("Bye!")
        exit()