#copying files
# copyfile() = copes content of a file
# copy() = copyfile() + permission mode + destination can be a directory
#copy2() = copy() + copy metadeta (file's creation and modification times)

import shutil
shutil.copy('testtext.txt','new.text') #src,destination 
shutil.copyfile('testtext.txt','new.text1') #src,destination 
shutil.copy2('testtext.txt','new.text2') #src,destination 