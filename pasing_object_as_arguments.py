#here we will pass object as arguments 


class Car:
      color = None

class motercycle:
       color = None

def change_color(vehicle , color):
        vehicle.color = color





car_1 = Car()
car_2 = Car()
car_3 = Car()

Motercycle = motercycle()

change_color(Motercycle , "black")

change_color(car_1,"red")

change_color(car_2,"blue")



print(car_1.color)
print(car_2.color)
print(car_3.color)

print(Motercycle.color)