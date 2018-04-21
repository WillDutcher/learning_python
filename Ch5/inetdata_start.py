#
# Example file for retrieving data from the internet
#

import urllib.request # Provides classes and code to make http requests

def main():
    webUrl = urllib.request.urlopen("http://www.google.com")
    print("result code: " + str(webUrl.getcode())) # Result code: 200 = everything is okay"
    data = webUrl.read() # return HTML of the page in question
    print(data)

if __name__ == "__main__":
  main()
