#multi-level inheritence - whan a deried (child )class inherits another derieved  (child class)  

class animal_kingdom():
    alive = True

class animals(animal_kingdom):
    def eat(self):
        print (" animal is eating ")

class dog(animals):
    def bark(self):
        print(" animal is barking ")
    def returner(self):
        return "hahahhahaha"

Dog= dog()
Dog.eat()
Dog.bark()
print(Dog.returner())