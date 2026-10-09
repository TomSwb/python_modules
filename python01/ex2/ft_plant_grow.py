
class Plant:
    def __init__(self, name, height, days, growth_rate):
        self.name = name
        self.height = height
        self.days = days
        self.growth_rate = growth_rate
        
    def show(self):
        print(f"{self.name}: {round(self.height)}cm, {self.days} days old")
        
    def grow(self)
        self.height += self.growth_rate
    
    def age(self)
        self.days += 1
    
class Garden:
    def __init__(self):
        self.plants = []
        
    def add_plant(self, plant):
        self.plants.append(plant)

    def display_plants(self):
        for plant in self.plants:
            self.plants.show()
            
    def display_one_plant_growth(self, name)
        
            
    def growing_plant(self)
        for plant in plants:
            self.plants.grow()
            self.plants.age()

def main():
    rose = Plant("Rose", 25, 30, 0.8)
    sunflower = Plant("Sunflower", 80, 45, 1.2)
    cactus = Plant("Cactus", 15, 120, 1.6)

    plant = Plant()
    garden = Garden()

    garden.add_plant(rose)
    garden.add_plant(sunflower)
    garden.add_plant(cactus)

    print("=== Garden Plant Growth ===")
    i = 1
    days = 5
    while i < days:
        print(f"=== Day{i} ===")
        garden.plant.grow("Rose")
        plant.show()
        i += 1
    print("Grows this week: {height} cm")

if __name__ == "__main__":
	main()

#!/usr/bin/env python3
# dont forget chmod 777 to make executable