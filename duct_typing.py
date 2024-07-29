#duct typing = concept where the class of an object is less important than the methords 
#               class type is not checked if minimum method/attributes are present 
#                  "if it walks like a duck , and it quaks like a duck , then it must be a duck "

class Duck :
    def walk(self):
        print("this duck is walking")

    def talk(self):
        print("this duck is quacking")

class Chicken :
    def walk(self):
        print("this chicken is walking")

    def talk(self):
        print("this chicken is clucking")

class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print ("the bird is caught")

person = Person()
duck= Duck()
chicken = Chicken()

person.catch(duck)
person.catch(chicken) # as chicken has the same methord/attributes as that of duck so it can also be printed insted of duck
