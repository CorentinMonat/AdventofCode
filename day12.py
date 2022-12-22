import numpy as np
np.set_printoptions(linewidth=np.inf)
np.set_printoptions(threshold=np.inf)
data = open("day12.txt").read().splitlines()
heightmap = np.zeros((len(data),len(data[0])), dtype = str)
# put data in a matrix
for i in range(len(data)):
    for j in range(len(data[0])):
        heightmap[i][j] = data[i][j]
        