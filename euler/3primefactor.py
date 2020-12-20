# program for finding largest prime factor of a given number

n = eval(input("Please enter the no to find the prime factors: "))
factors = []
for i in range(1,n):
    if(n%i == 0):
        factors.append(i)

print("The factors of the given number are :",factors)

prime = []
k = 0
for i in range(2, len(factors)):
    if(factors[k]%i != 0):
        prime.append(factors[k])
    k = k+1



print(prime)
