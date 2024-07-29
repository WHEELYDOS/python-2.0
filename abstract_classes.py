# it prevents a user from creating a object of that class
#  + compels a user to override abstract methords in a chil class 

# abstract class=   a class wich contains one or more abstract methord 
# abstract methord =   a methord that has declaration but no implimentation .

from abc import ABC , abstractmethod #abc stands for abstract base class

class vehicle:
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def lmao(self):
        pass

class car (vehicle):
    def go(self):
        print("the car is going")
    
    def stop(self):
        print("stoping the car")


class motercycle(vehicle):
    def go(self):
        print("the motercycle is moving")
    
    def stop(self):
        print("stoping the motercycle")

Vehicle = vehicle()
Car = car()
Motercycle = motercycle()

#Vehicle.go() # cannot call go or stop methord but can call lmao cause it is not a abstractmethods
Vehicle.lmao()
Car.go()
Motercycle.go()

Car.stop()
Motercycle.stop()