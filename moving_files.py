import os 

source = "helow.txt" # make a hwlow file to run this code
destination = "E:\\codess\\helow.txt"

try: 
    if os.path.exists(destination):
        print ("there is already a file there")
    else:
        os.replace(source,destination)
        print (source + " has been moved to the destination")
except FileNotFoundError:
    print("file not found")



