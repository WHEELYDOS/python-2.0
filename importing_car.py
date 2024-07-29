from car import Car
 
new_car = Car("audi","rmx07",2024,"matte black")
new_car1 = Car("ford","musstang",2022,"matte white")

print(new_car.make)
print(new_car.model)
print(new_car.year)
print(new_car.color)

new_car.drive()
new_car.stop()


print(new_car1.make)
print(new_car1.model)
print(new_car1.year)
print(new_car1.color)

new_car1.drive()
new_car1.stop()


print(new_car.wheels)
print(new_car1.wheels)

new_car.wheels = 2 
print(new_car.wheels)
