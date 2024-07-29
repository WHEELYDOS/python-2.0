class Car:
   
    wheels = 4 #it will be used as default value     #class variable

    def __init__(self , make , model , year , color): # __init__ is used to contruct object also known as constructor
        self.make = make  #instance varriable
        self.model = model #instance varriable
        self.year = year #instance varriable
        self.color = color #instance varriable


    def drive(self):
        print (" this "+ self.model+" is driving now ")
    
    def stop (self):
        print (" this " + self.model + " car stopped")

    
    pass