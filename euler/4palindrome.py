#program for largest palindrome product of 3 digit numbers

def palindrome(number):
    num = str(number)
    numb = num[::-1]

    if(num == numb):
        return True
    else:
        return False

pal = []

for i in range(100,1000):
    for j in range(100,1000):
        m = i*j
        if(palindrome(m) == True):
            pal.append(m)

print("Max polindrome is:  ", max(pal))
