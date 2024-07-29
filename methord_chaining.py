# methiord chaining = calling multiple methords sequentially
#                     each cell performs an action on the same object and return self

class car:
    def turn_on(self):
        print(" engine has been turned on  - ratatatata") 
        return self
    
    def drive(self):
        print(" car is driving vrooooomm vrroooommmm") 
        return self
    
    def breaks(self):
        print(" brakes has been engaged chiiiiiiiiiiiiiiiiiiiii...(tyers sliding)") 
        return self

    def turn_off(self):
        print(" engine has been turned off  poof") 
        return self
print("------------------------------------------------------------------------------")
Car = car()
Car.turn_on()
Car.drive()

print("------------------------------------------------------------------------------")
Car.turn_on().drive() # return self statement return the value after executing turn on and then that 
                        #self value goes into second methord that is drive
print("------------------------------------------------------------------------------")
Car.breaks().turn_off()
print("------------------------------------------------------------------------------")

Car.turn_on().drive().breaks().turn_off()#can be also written as 
print("------------------------------------------------------------------------------")
Car.turn_on()\
    .drive()\
    .breaks()\
    .turn_off()
print("------------------------------------------------------------------------------")