class animal :
    alive = True
    
    #def __init__(self,name) :
    #   self.name= name
        


    def eating(self):
        print( "this animmal is eating ")
    def sleeping(self):
        print("this animal is sleeping ")
class rabbit(animal):
    def jump():
        print("this rabbit is jumpoing")
    pass
class fish(animal):
    def swim():
        print("this fish is swiming")
    pass
class deer(animal):
    def run():
        print("this deer is running")
    pass
Rabit = rabbit()
Fish = fish()
Deer = deer()
print(Rabit.alive)
Fish.eating()
Deer.sleeping()
fish.swim()

#new = animal("cutie")
#new.eating()

# all the hastag will only work with each other it is a concept of parent class


