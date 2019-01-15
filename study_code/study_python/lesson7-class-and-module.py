#>28 class and its inherit
class Car():
    """Car class"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  #initialize

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + 'self.make' + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cannot roll back an odometer!')

    def increment_odometer(self,miles):
        self.odometer_reading +=miles

    def fill_gas_tank(self):
        print("This car's tank has been filled!")
#inherit example 1
class ElectricCar(Car):
    """ElectricCar class inherit"""
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 70

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-KWh battery.')

    def fill_gas_tank(self):
        print("Electric car has no tank")
#inherit example 2
class Battery():
    """Battery class"""
    def __init__(self,battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('This car has a ' + 'str(self.battery_size)' + '-KWh battery.')

    def get_range(self):
        """indicate the total miles on a full charge"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)

class ElectricCar(Car):
    """pull out Battery class"""
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

my_tesla = ElectricCar('telsa','models s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#class module import
#module_file has the specific class definition
import module_file
object = module_file.class_name()
from module_file import class_name
from module_file import class_name1,class_name2,class_name3
object = class_name()
from module_file import * #import all class from module
