# solution 1
'''f = open('/home/konam/Desktop/input.txt','r')

contents = f.readlines()

suml = 0
for line in contents:
    i = eval(line)
    suml = suml + i

print(str(suml)[:10])

'''
# solution 2
data = '/home/konam/Desktop/input.txt'

print (str(sum(int(x) for x in open(data,'r')))[:10])
