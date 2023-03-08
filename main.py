class Vehicle:
    def __init__(self,model,make,year_manufacture):
        self.model = model
        self.make = make
        self.year_manufacture=year_manufacture
        
    def car_details(self):
        print(self.model,self.make,self.year_manufacture)
        
class Saloon_cars(Vehicle):
    def saloondetails(self):
        print(self.model)
