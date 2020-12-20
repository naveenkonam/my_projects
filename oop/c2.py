class Parrot:
    pass


# instaniate the parrot class
blue = Parrot()
green = Parrot()

blue.name = "Blue"
blue.age = 6


green.name = "Green"
green.age = 7

# access the instance attributes
print("{} parrot is {} years old".format(blue.name,blue.age))
print("{} parrot is {} years old".format(green.name,green.age))

# end of the file
