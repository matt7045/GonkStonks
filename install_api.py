import zipfile
import wget

url      = "https://download2.interactivebrokers.com/portal/clientportal.gw.zip"
filename = wget(url)
# Create a ZipFile Object and load sample.zip in it
with ZipFile(filename, 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()
