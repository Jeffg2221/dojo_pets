from ninja import Ninja
from pet import Pet





my_treats = ['Sausage', 'Bacon', 'Trash Bag']
my_pet_food = ['Pizza', 'Burger']

king = Pet("King", "Dog",["Roll Over", "Sit"], "Barking!!")

jeff = Ninja("Jeff", "Gomez", my_treats, my_pet_food, king)

jeff.feed()
jeff.feed()
jeff.feed()

jeff.walk()
jeff.walk()
jeff.bathe()
