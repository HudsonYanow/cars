class Car:
    def __init__(self, brand, model, year, color, price, gasLevel, gasTankSize, gasMileage, carMileaeg):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.gasLevel = gasLevel
        self.gasTankSize = gasTankSize
        self.gasmileage= gasMileage
        self.carmileaeg= carMileaeg
    def drive(self, distance):
        print(f"I am driving a {self.brand} {self.model} {self.year} {self.color} car. distance driven {distance} miles.")
        self.gasLevel=self.gasLevel-distance/self.gasmileage
        self.carmileaeg=self.carmileaeg+distance
        print(self.gasLevel)
    def fillgas(self,gas):
        self.gasLevel=self.gasLevel+gas
    def upgrade(self):
        if self.gasmileage<=20:
            self.gasmileage*=2
car1= Car("toyota", "chr", 1968, "black", 20000, 0.75, 15, 25, 2000)
car2= Car("toyota", "bmw", 1969, "silver", 50000, 0.5, 20, 20, 2000)
car1.drive(10)
car2.drive(20)    
car1.price=1000
del car2.price
car1.fillgas(10)
