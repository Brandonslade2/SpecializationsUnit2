import csv
from abc import ABC, abstractmethod
from pprint import pprint

def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "frosting", "cake", "filling", "sprinkles"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)


#Part 4 Content:

#Commented out sections are from previous steps, but not for deployment, to show proof that I did them.

class Cupcake:
    size = "regular"
    def __init__(self, name, price, frosting, cake, filling):
        self.name = name
        self.price = price
        self.frosting = frosting
        self.cake = cake
        self.filling = filling
        self.sprinkles = []
    
    def add_sprinkles(self, *args):
        for i in args:
            self.sprinkles.append(i)
    
    @abstractmethod
    def calculate_price(self, quantity):
        return self.price*quantity
    
class Mini(Cupcake):
    size = "mini"
    def __init__(self, name, price, frosting, cake):
        self.name = name
        self.price = price
        self.frosting = frosting
        self.cake = cake
        self.sprinkles = []

"""
my_cupcake_mini = Mini("Chocolate", 1.99, "Chocolate", "White")

print(my_cupcake_mini.name)
print(my_cupcake_mini.price)
print(my_cupcake_mini.size)


audrey_favorite_cupcake = Cupcake("The Audrey Special", 1.99, 'Chocolate', 'Red velvet', False)

audrey_favorite_cupcake.frosting = "Vanilla"
audrey_favorite_cupcake.filling = True
audrey_favorite_cupcake.name = "The Audrey Special 2"

audrey_favorite_cupcake.is_miniature = False

audrey_favorite_cupcake.add_sprinkles("Green")

print(audrey_favorite_cupcake.calculate_price(4))
"""

def read_csv(file):
    with open("sample.csv") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

""" 
FROM PREVIOUS STEP BUT NOT FOR DEPLOYMENT:
read_csv("sample.csv")

cupcake1 = Cupcake("Stars and Stripes", 2.99, "Vanilla", "Vanilla", "Vanilla")
cupcake1.add_sprinkles("Red", "White", "Blue")
cupcake2 = Mini("Oreo", .99, "Chocolate", "Cookies and Cream")
cupcake2.add_sprinkles("Oreo pieces")

cupcake_list = [
    cupcake1,
    cupcake2,
]
"""

def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "frosting", "cake", "filling", "sprinkles"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "frosting": cupcake.frosting, "cake": cupcake.cake, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "frosting": cupcake.frosting, "cake": cupcake.cake, "sprinkles": cupcake.sprinkles})


#write_new_csv("sample.csv", cupcake_list)



def add_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "frosting", "cake", "filling", "sprinkles"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if hasattr(cupcake, "filling"):
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "frosting": cupcake.frosting, "cake": cupcake.cake, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
        else:
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "frosting": cupcake.frosting, "cake": cupcake.cake, "sprinkles": cupcake.sprinkles})