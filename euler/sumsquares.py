# project euler problem no 6: Sum square difference

def sumsq(n):
    squares_n = []
    sum_n = []

    for i in range(n+1):
        squares_n.append(i**2)
        sum_n.append(i)

    diff = (sum(sum_n)**2)-sum(squares_n)
    return diff


i = eval(input("Enter the no upto which sum square difference to be calculated: "))

print("The sum square difference of {} is {}".format(i,sumsq(i)))
