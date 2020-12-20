class Parrot:

    # class attribute
    species = "bird"

    # instance attributes
    def __init__(self,name,age):
        self.name = name
        self.age = age


# instaniate the parrot class
blue = Parrot("Blue",5)
green = Parrot("Green",6)

# access the class attributes
print("Blue is a {}".format(blue.species))
print("Green is a {}".format(green.species))

# access the instance attributes
print("{} is {} years old".format(blue.name,blue.age))
print("{} is {} years old".format(green.name,green.age))

# end of the file
