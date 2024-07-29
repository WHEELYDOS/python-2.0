import os
import shutil
src="delete.txt"
try:
    os.remove(src) #deletes a file 
    #os.rmdir() # deletes a empty files #rmdir()- remove directory 
    #shutil.rmtree() #deletes the directory and all the files within
    print("src removed")

except FileNotFoundError:
    print("file not found")

except TypeError:
    print("file does not exist with the given name")