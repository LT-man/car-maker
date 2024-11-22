class Car():
    
    def __init__(self, color, model, name, engine, turbo, wheels, interior, brakes, exhaust, tyres, lights, plastic, seats, air_conditing, material, speed):
        self.color = color
        self.model = model
        self.name = name
        self.engine = engine
        self.turbo = turbo
        self.wheels = wheels
        self.interior = interior
        self.brakes = brakes
        self.exhaust = exhaust
        self.tyres = tyres
        self.lights = lights
        self.plastic = plastic
        self.seats = seats
        self.air_conditing = air_conditing
        self.material = material
        self.speed = speed
    #getters methods
    def get_tyres(self):
        print(self.tyres)
    #setters methods
    def set_name(self):
        self.name = input(" Enter brand name")
    #customs methods
    def increase_speed(self):
        self.speed += 10
        print("speed increaser")
    def decrease_speed(self):
        self.speed -= 10
        print("speed decreaser")

#making a object of the car
bumbini = Car("black", "koenigsegg", "jesko absolut", "20L V16", "quad turbo", "5 spoke", "brown leather", "Carbon cermaic brembo", "quad tips", "michelin all season 22inch", "blue and white step underglow tinted headlights and taillights", "black premium quality plastic", "carbon fiber bucket seats", "premium quaility air", "carbon fiber", 563)
bumbini.increase_speed()
bumbini.get_tyres()
bumbini.set_name()