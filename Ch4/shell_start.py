#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
  # make a duplicate of an existing file
  if path.exists("textfile.txt"): # make sure file exists
    # get the path to the file in the current directory
    src = path.realpath("textfile.txt") # Source of the original file

    # let's make a backup copy by appending "bak" to the name
    dst = src + ".bak" # gets path to original file and appends a ".bak" to end

    # copy over the permissions, modification times, and other info
    # shutil.copy(src, dst) # Use shell utility to create a copy of that file; only copies file contents, not mod data
    # shutil.copystat(src, dst)

    # rename the original file
    # os.rename("textfile.txt", "newfile.txt")

    # now put things into a ZIP archive
    # root_dir, tail = path.split(src)
    # shutil.make_archive("archive", "zip", root_dir)

    # more fine-grained control over ZIP files
    with ZipFile("textzip.zip", "w") as newzip:
        newzip.write("textfile.txt")
        newzip.write("textfile.txt.bak")

if __name__ == "__main__":
  main()
