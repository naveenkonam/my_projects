
def countstr(str):
    
    if(len(str)==0):
        print("You have not entered anything, please enter")
    else:
        print(str, "has", len(str), "characters")

in_str = input("Enter the string: ")

countstr(in_str)
