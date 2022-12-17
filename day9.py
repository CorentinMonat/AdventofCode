import numpy as np
# data = open("day9.txt").read().splitlines()
data = ['R 4', 'U 4', 'L 3', 'D 1', 'R 4', 'D 1', 'L 5', 'R 2']

grid = np.zeros((10,10), dtype='str')

direction = []
number_of_steps = []
# get directions and number of steps for each line
for i in range(len(data)):
    dir, num = data[i].split(" ")
    direction.append(dir)
    number_of_steps.append(int(num))
    
# Have H move to correct place
grid[-1][0] = 'H'

            