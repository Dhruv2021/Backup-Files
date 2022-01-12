import os
import shutil

source=input("Enter The Source Folder Name= ")
destination=input("Enter The Destination Folder= ")

source=source+"/"
destination=destination+"/"

listoffiles=os.listdir(source)
for file in listoffiles:
    shutil.copy((source+file),destination)