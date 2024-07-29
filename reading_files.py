try: 
    with open('E:\\codess\\files to be read by python\\readme.txt') as file : #if the file is in the location of the pythom file 
                                                                               #then u only need to write the name and its extention
                print(file.read())
except FileNotFoundError:
        print("file is not found at the given location :)")#prints exception 