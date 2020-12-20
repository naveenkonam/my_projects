def fact(n):
    factorial = 1
    if n==0:
        return 1
    elif n>0:
        factorial = factorial * n * fact(n-1)
        return factorial
    else:
        print("Please enter a positive number")


x = eval(input("Please enter a number to find the factorial: "))
ans = fact(x)
print("factorial of {} is {} \n".format(x, fact(x)))

ans_str = str(ans)
s = 0
for n in ans_str:
    s = s + eval(n)
print("Sum of number in {} factorial is {}\n".format(x,s))



