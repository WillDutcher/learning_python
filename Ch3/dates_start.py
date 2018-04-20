#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print("Today's date is: ", today)

  # print out the date's individual components
  day = today.day
  month = today.month
  year = today.year
  print("Day: ", day)
  print("Month: ", month)
  print("Year: ", year)

  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("Today's weekday number is: ", today.weekday())
  days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
  print("Which is a ", days[today.weekday()])

  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.now()
  print("The current date and time is:", today)

  # Get the current time
  t = datetime.time(datetime.now())
  print(t)


if __name__ == "__main__":
  main();
