class Car:
    tax = 1
    def __init__(self,brand , model, founded_year, price):
        self.brand = brand
        self.model = model
        self.founded_year = founded_year
        self.price = price
        
    def Brand(self):
        return self.brand
    def GetValue(self):
        return(self.price * Car.tax)
Car.tax = 2 
car_1 = Car("Vinfast","LuxA", 2017,1000)
car_2 = Car("BMW" ,"i320",1916,700)
print(f"{car_1.model} price {car_1.GetValue()} $")
print(f"{car_2.model} price{car_2.GetValue()} $")

        