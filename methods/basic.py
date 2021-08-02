"""
copy, move, delete functions
"""
import os
import shutil
#from methods import platforms
from GWEN.methods import platforms
from Kingfish.Core import logger

"""
Tells the user how to insert path according to his OS
"""
def pathPattern():
    if platforms.osType() == "windows":
        print("Path pattern: C:\\path\\to\\file")
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

    def copy_file(self, source = None, destination = None):
        pathPattern()
        if not source:
            source = input("Insert the source path (including the file): ")
        if not destination:
            destination = input("Insert the destination path: ")
        try:
            shutil.copy(str(source), str(destination))
            logger.info("File has been copied to {}".format(str(destination)))
        except:
            logger.fatal("Couldn't do the operation. Please check your inserted paths.")

    """
    Get from the user path to a folder and destination.
    """

    def copy_folder(self):
        pathPattern()

        source = input("Insert the source path: ")
        destination = input("Insert the destination path: ")
        try:
            shutil.copytree(str(source), str(destination))
            logger.info("Folder has been copied to {}".format(str(destination)))
        except:
            logger.fatal("Couldn't do the operation. Please check your inserted paths.")

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
            logger.info("File has been moved to {}".format(str(destination)))
        except:
            logger.fatal("Couldn't do the operation. Please check your inserted paths.")

    """
    Gets a file to delete
    """
    
    def delete_file(self):
        pathPattern()

        source = input("Insert the source path (including the file): ")

        if os.path.isfile(str(source)):
            os.remove(str(source))
            logger.info("File has been removed")
        else:
            logger.fatal("Inserted path is incorrect")

    """
    Deletes a folder
    """

    def delete_folder(self):
        pathPattern()

        source = input("Insert the source path: ")

        if os.path.isdir(str(source)):
            os.rmdir(str(source))
            logger.info("Folder has been removed")
        else:
            logger.fatal("Inserted path is incorrect")

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

    """
    Creates a file in a specific destination
    """

    def create_file(self):
        pathPattern()

        source = input("Insert a directory: ")
        extension = input("Insert the file type (extension): ")
        name = input("Insert the file name: ")

        file_name = source + '\\' + name + '.' + extension
        file = open(file_name, "w+")

        edit = input("Would you like to write something in the file?")
        if edit == 'yes' or 'y':
            content = input("Type your input: ")
            file = open(file_name, "a+")
            file.write(content)
            logger.info("{} has been created".format(file_name))
        else:
            logger.info("Ok, {} is an empty file for now".format(file_name))

    def name_manipulator(self):
        """
        Replaces parts of names
        example: name_manipulator("serhio", "kopo")
        """
        source = input("Insert a directory: ")
        old_str = input("Enter the sequence you would like to change: ")
        new_str = input("Enter the sequence you would like to set instead: ")

        for root, dirs, files in os.walk(source):
            for name in files:
                new_name = name.replace(old_str, new_str)
                os.rename(os.path.join(root, name), os.path.join(root, new_name))
                print(f"{name} changed to {new_name}")

    def dir_info(self):
        """
        Returns number of files in directory
        """
        source = input("Insert a directory: ")
        number_of_files = len([files for root, dirs, files in os.walk(source) for name in files if os.path.isfile(os.path.join(root, name))])
        print(f"There are {number_of_files} files in {source}")
        return number_of_files

    def copy_directory(self, source = None, destination = None):
        if not source:
            source = input("Insert the source path (including the file): ")
        if not destination:
            destination = input("Insert the destination path: ")
        name = ""
        for char in source[::-1]:
            if char != "\\":
                name += char
            else:
                break
        formatted_name = name[::-1]
        shutil.copytree(source, os.path.join(destination, formatted_name))
        logger.info(f"Successfully copied {source} content to {destination}")

    def exit(self):
        logger.info("Bye!")
        exit()
