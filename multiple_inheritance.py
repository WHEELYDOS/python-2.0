#multiple inharitance - when the child class is derived from one or more parent class

class prey():
    def flee(self):
        print("this animal will flee")

class predator():
    def hunt(self):
        print("this animal will hunt")

class rabit(prey):
    pass

class lion(predator):
    pass

class fish(prey,predator):
    pass

Rabbit = rabit()

Lion = lion()

Fish = fish()

Rabbit.flee()

Lion.hunt()

Fish.flee()
Fish.hunt()