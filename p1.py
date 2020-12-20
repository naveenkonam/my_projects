class Myclass:
    def __init__(self,roll_no):
        self.roll = roll_no
    def section(self):
        print("Welcome to Section and your roll no is: ",self.roll)
        pass

ramu = Myclass(10)
ramu.section()
