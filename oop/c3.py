class Parrot:

    # class attribute
    species = "bird"

    # instance attributes
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # instance behaviours
    def sing(self,song):
        return("{} parrot is singing {}".format(self.name,song))

    def dance(self):
        return("{} parrot is dancing".format(self.name))


# instaniate the parrot class
blue = Parrot("Blue",5)
green = Parrot("Green",6)

# access the class attributes
print("Blue parrot is a {}".format(blue.species))
print("Green parrot is a {}".format(green.species))

# access the instance attributes
print("{} parrot is {} years old".format(blue.name,blue.age))
print("{} parrot is {} years old".format(green.name,green.age))

print(blue.sing("Happy"))
print(green.dance())

# end of the file
