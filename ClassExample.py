
class Car:
    def __init__(self,color,miles):
        self.color = color
        self.miles= miles
    def details(self):
        return f"The {self.color} car has {self.miles} miles"
    
blue_car =Car(color="blue",miles=20000)
red_car = Car(color="red",miles=30000)

print(blue_car.details())
print(red_car.details())