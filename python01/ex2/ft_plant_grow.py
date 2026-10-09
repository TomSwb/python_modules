
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        
    def show(self):
        print(f"{self.name}: round({self.height})cm, {self.age} days old")
        
    def grow(self, days)
        if name == rose:
            self.height += 0.8 * days
        elif name == sunflower:
            self.height += 1.2 * days
        elif name == cactus:
            self.height += 1.6 * days
    
    def age(self, days)
        self.age += days
    
class Garden:
    def __init__(self):
        self.plants = []
        
    def add_plant(self, plant):
        self.plants.append(plant)

    def display_plants(self):
        for plant in self.plants:
            self.plants.show()

def main():
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    garden = Garden()

    garden.add_plant(rose)
    garden.add_plant(sunflower)
    garden.add_plant(cactus)

    print("=== Garden Plant Registry ===")
    garden.display_plants()

if __name__ == "__main__":
	main()

#!/usr/bin/env python3
# dont forget chmod 777 to make executable