import os
os.chdir(r'C:\Users\Bob\Documents\GitHub\Advent_2019\Advent_2019_1a')

fuel = 0

def fuelIncrement(localFuel):
    residual = (localFuel // 3 ) - 2
    delta = residual
    while residual > 5:
        residual = (residual // 3 ) - 2
        delta = delta + residual
#        print('residual is %s' % residual)
    return delta
   

weight = open('Input_1a.txt', 'r')
for line in weight:
    fuel = fuel + fuelIncrement(int(line))
##    print(' ')
##    print(line)
##    print(fuelIncrement(int(line)))
weight.close()

print(fuel)

