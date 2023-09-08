class Vehicle:
    def __init__(self):
        raise NotImplementedError("Do not create raw Vehicle objects.")
    def __str__(self):
        return self.name

class Motocycle(Vehicle):
    def __init__(self):
        self.name="charley"
        self.wheels = 2

class Car(Vehicle):
    def __init__(self):
        self.name="toyota"
        self.wheels = 4


vehicle1 = Vehicle()
vehicle2 = Motocycle()
vehicle3 = Car()
