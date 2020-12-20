class Parrot:

    def fly(self):
        print("parrots can fly")

    def swim(self):
        print("Parrots can't swim")



class Penguin:

    def fly(self):
        print("Penguins can't fly")

    def swim(self):
        print("Penguins can swim")

def flying_test(bird):
    bird.fly()

blu = Parrot()
peggy = Penguin()

flying_test(blu)
flying_test(peggy)
