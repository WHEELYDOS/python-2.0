# walrush operator := 
# new to python 3.8
# asignment expression aka walrush operation 
# assign values to variable as a part of a large expression 

happy = True 
print (happy)

#walrush operater 
print(happy:= True)

foods = list()

while  True:
    food = input("enter the name of food you like : ")
    if food == "quit":
        break
    foods.append(food)

for i in foods:
    print(i)
foods.clear()

print("-----------------------------------------------------")

foods = list()
while food :=input("add ur fav dish to the list  : ") != "quit" : 
    foods.append(food)

for i in foods:
    print(i)
