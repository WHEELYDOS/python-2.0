import os 
paths = "C:\\Users\\harsh\\OneDrive\\Desktop\\codes.txt" # u need to add doble slashes in order to ensure that it will read
                                                #the location on the computer it wont work with the single '\'

if os.path.exists(paths): # chekes that if the loction exist or not
    print("location exists ")
    if os.path.isfile(paths): #check if the given location is occipies by file or not 
        print("it is a file")
    elif os.path.isdir(paths):#chak if the located file is a directory(folder) or not
        print("it is a directory")
else:
    print("location does not exists ")
    