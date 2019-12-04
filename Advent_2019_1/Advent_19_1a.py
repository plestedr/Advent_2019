import os
os.chdir(r'C:\Users\Bob\Documents\GitHub\Advent_2019\Advent_2019_1a')

fuel = 0

def fuelIncrement(localFuel):
    return (localFuel // 3 ) - 2
   

weight = open('input_1a.txt', 'r')
for line in weight:
    fuel = fuel + fuelIncrement(int(line))
#    fuel = int(line)
#    print(fuelIncrement(int(line)) )
weight.close()

print(fuel)

