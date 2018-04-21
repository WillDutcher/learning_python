#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
  print(os.name)

  # Check for item existence and type
  print("Item exists: " + str(path.exists("textfile.txt"))) # Test if item exists
  print("Item is a file: " + str(path.isfile("textfile.txt"))) # Test if item is a file
  print("Item is a directory: " + str(path.isdir("textfile.txt"))) # Test if item is a directory

  # Work with file paths
  print("Item path: " + str(path.realpath("textfile.txt"))) # Get file path
  print("Item path and name: " + str(path.split(path.realpath("textfile.txt")))) # Get file path and file name

  # Get the modification time
  t = time.ctime(path.getmtime("textfile.txt")) # Convert modification time to real time of file
  print(t)
  print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))) # Different way to get same result, above

  # Calculate how long ago the item was modified
  td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
  print("It has been " + str(td) + " since the file was modified.")
  print("Or, " + str(td.total_seconds()) + "seconds.")


if __name__ == "__main__":
  main()
