import re
import numpy as np
np.set_printoptions(linewidth=np.inf)
np.set_printoptions(threshold=np.inf)
# data = open("day15.txt").read().splitlines()
data = open("day15test.txt").read().splitlines()
Xsensor = []
Ysensor = []
Xbeacon = []
Ybeacon = []

for i in range(len(data)):
    a = [int(d) for d in re.findall(r'-?\d+', data[i])]
    Xsensor.append(a[0])
    Ysensor.append(a[1])
    Xbeacon.append(a[2])
    Ybeacon.append(a[3])
    
# find minimum X value
if min(Xsensor) > min(Xbeacon):
    minX = min(Xbeacon)
else:
    minX = min(Xsensor)
    
# find minimum Y value
if min(Ysensor) > min(Ybeacon):
    minY = min(Ybeacon)
else:
    minY = min(Ysensor)

# find maximum X value
if max(Xsensor) < max(Xbeacon):
    maxX = max(Xbeacon)
else:
    maxX = max(Xsensor)
    
# find maximum Y value
if max(Ysensor) < max(Ybeacon):
    maxY = max(Ybeacon)
else:
    maxY = max(Ysensor)

# to number columns of the array
a = np.linspace(minX,maxX,-minX+maxX+1)
print([a])
# mapping of the thingy were sources S and beacons B are
mapping = np.zeros((-minY+maxY+1,-minX+maxX+1), dtype=str) # this is too big for the real data set :(
mapping.fill('.')

# Place sensors
for i in range(len(Xsensor)):
    mapping[Ysensor[i]-minY][Xsensor[i]-minX] = 'S'
# Place beacons
for i in range(len(Xbeacon)):
    mapping[Ybeacon[i]-minY][Xbeacon[i]-minX] = 'B'

print([mapping])


