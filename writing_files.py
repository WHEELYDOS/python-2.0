text = "yo \n this is a new text file \n have a good day ahead " #\n addes new lines
new_text = "\nhello i am the new one"

with open ('testtext.txt','w') as file: #bydefault 'r' - for rading  and 'w' - is for writing and 'a' - is to append (adss in the current file )
   file.write(text) #it also creats  a file if there isnt any of the current name

with open ('testtext.txt','a') as file:
    file.write(new_text)