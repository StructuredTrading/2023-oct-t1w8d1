class Car:
    # constructor
    def __init__(self, color, make):
        self.color = color
        self.make = make
        print("hello")

    def get_color(self):
        return self.color
    
    def set_solor(self, color):
        self.color = color

    def run(self):
        print(f"{self.make} is running!! Vrooooom vrrroooooommmmmm!!!!!")




my_car = Car("black", "honda")
print(my_car.color, my_car.make)
my_car.run()
my_car.color = 'purple'
print(my_car.color)

your_car = Car("red", "Ferrari")

print(your_car.color, your_car.make)
your_car.run()


class PetrolCar(Car):
    def __init__(self, color, make, capacity_of_tank):
        self.capacity_of_tank = capacity_of_tank
        super().__init__(color, make)


my_petrol_car = PetrolCar("silver", "BMW", 40)

print(my_petrol_car.capacity_of_tank)
print(f"My {my_petrol_car.color} {my_petrol_car.make}, has a {my_petrol_car.capacity_of_tank}L tank")


class ElectricCar(Car):
    # Overriding
    def run(self):
        print("I run silently. No Vrroooming!!")


my_electric_car = ElectricCar("Yellow", "Tesla")

my_electric_car.run()