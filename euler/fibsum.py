# Project Euler: problem 2 - Even Fibonacci numbers

x,y = 0,1
fib = []

fib.append(x)
z = eval(input("Please enter upto which numbers does the Fibonacci sequence required? "))
while y<z:
    fib.append(y)
    x,y = y,x+y

print("the fibonacci sequence upto {} is ".format(z),fib)

fibsum = 0
for i in range(0,len(fib)):
    if ((fib[i]%2) == 0):
        fibsum = fibsum + fib[i]

print("the even sum of fib sequence upto {} is: {}".format(z,fibsum))
