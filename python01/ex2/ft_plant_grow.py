
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        
    def show(self):
        print(f"{self.name}: round({self.height})cm, {self.age} days old")
        
    def grow(self)
        if name == rose:
            self.height += 0.8
        elif name == sunflower:
            self.height += 1.2
        elif name == cactus:
            self.height += 1.6
    
    def age(self)
        self.age += 1
    
class Garden:
    def __init__(self):
        self.plants = []
        
    def add_plant(self, plant):
        self.plants.append(plant)

    def display_plants(self):
        for plant in self.plants:
            self.plants.show()
            
    def growing_garden(self)
        self.plants.grow()
        self.plants.age()
        self.plants.show()

def main():
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    garden = Garden()

    garden.add_plant(rose)
    garden.add_plant(sunflower)
    garden.add_plant(cactus)

    print("=== Garden Plant Growth ===")
    garden.show()
    i = 1
    days = 5
    while i < days:
        print(f"=== Day{i} ===")
        garden.growing_garden()
    print("")

if __name__ == "__main__":
	main()

#!/usr/bin/env python3
# dont forget chmod 777 to make executable