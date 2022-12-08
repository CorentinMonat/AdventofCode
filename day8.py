import re
import numpy as np
data = open("day8.txt").read().splitlines()
# data = ['30373', '25512', '65332', '33549', '35390']
forest = np.zeros((len(data),len(data[0])), dtype=None)

rowLeftToRight = data
rowRightToLeft = []
for i in range(len(rowLeftToRight)):
    rowRightToLeft.append(rowLeftToRight[i][::-1])

columnTopToBottom = []
for i in range(len(data[0])):
    forlist = ""
    for j in range(len(data)):
        toadd = data[j][i]
        forlist += toadd
    columnTopToBottom.append(forlist)
        
columnBottomToTop = []
for i in range(len(columnTopToBottom)):
    columnBottomToTop.append(columnTopToBottom[i][::-1])
    
# Part 1
# Look at list of numbers from left to right, set first one as max. If next number is higher, add number to matrix of whole forest 
# AND set that number as the new max! Go through the whole list. 
# Then do the same for the other three lists.
# (Exact same code because they will also be lists of numbers from left to right. 
# Only different thing is where the number needs to be added in the forest)

forest[0] = 1
forest[-1] = 1
for i in range(1,len(data)-1):
    forest[i][0] = 1
    forest[i][-1] = 1

# print('Looking from LEFT to RIGHT')
for i in range(1,len(rowLeftToRight)-1):
    maximum = rowLeftToRight[i][0]
    # print('New row! Maximum is now', maximum)
    for j in range(1,len(rowLeftToRight[i])-1):
        if rowLeftToRight[i][j] > maximum:
            # print(rowLeftToRight[i][j], 'is bigger than', maximum)
            maximum = rowLeftToRight[i][j] 
            forest[i][j] = 1
            # print('adding nummber to forest')
            # print(forest)
            # print('setting new maximum to', maximum)

# print('Looking from RIGHT to LEFT')
for i in range(1,len(rowRightToLeft)-1):
    maximum = rowRightToLeft[i][0]
    # print('New row! Maximum is now', maximum)
    for j in range(1,len(rowRightToLeft[i])-1):
        if rowRightToLeft[i][j] > maximum:
            # print(rowRightToLeft[i][j], 'is bigger than', maximum)
            maximum = rowRightToLeft[i][j] 
            forest[i][-j-1] = 1
            # print('adding number to forest')
            # print(forest)
            # print('setting new maximum to', maximum)
            
# print('Looking from TOP to BOTTOM')
for i in range(1,len(columnTopToBottom)-1):
    maximum = columnTopToBottom[i][0]
    # print('New column! Maximum is now', maximum)
    for j in range(1,len(columnTopToBottom[i])-1):
        if columnTopToBottom[i][j] > maximum:
            # print(columnTopToBottom[i][j], 'is bigger than', maximum)
            maximum = columnTopToBottom[i][j] 
            forest[j][i] = 1
            # print('adding number to forest')
            # print(forest)
            # print('setting new maximum to', maximum)
        
# print('Looking from BOTTOM to TOP')
for i in range(1,len(columnBottomToTop)-1):
    maximum = columnBottomToTop[i][0]
    # print('New column! Maximum is now', maximum)
    for j in range(1,len(columnBottomToTop[i])-1):
        if columnBottomToTop[i][j] > maximum:
            # print(columnBottomToTop[i][j], 'is bigger than', maximum)
            maximum = columnBottomToTop[i][j] 
            forest[-j-1][i] = 1
            # print('adding number to forest')
            # print(forest)
            # print('setting new maximum to', maximum)
            
answer1 = forest.sum()
print('the number of visible trees is', answer1) #putain ça marche bordel! :D

# Part 2

# omg how can I do this???
# take 
forest1 = np.zeros((len(data),len(data[0])), dtype=None)
    
    
for i in range(len(rowLeftToRight)): 
    for j in range(0,len(rowLeftToRight[0])):
        forest1[i][j] = data[i][j]
        
countsPerTree = np.ones((len(data),len(data[0])), dtype = None)

# to check left and right
for i in range(1,len(forest1)-1): #len(forest1) gives the number of rows in the matrix
    # print('changing to row', i)
    for j in range(1,len(forest1[0])-1): #len(forest1[0]) gives the number of columns in the matrix
        # print('changing to column', j)
        maximum1 = forest1[i][j] 
        count = 0
        # look right
        for k in range(j+1,len(rowLeftToRight)):
            # print('looking at column', k, ', maximum is', maximum1)
            if maximum1 > float(rowLeftToRight[i][k]):
                # print(maximum1, 'is bigger than', rowLeftToRight[i][k])
                count += 1
                # print('count is' ,count)
                if k == len(rowLeftToRight)-1:
                    # print('reached end of forest')
                    # print('final count is', count)
                    countsPerTree[i][j] *= count 
                    count = 0
                    break
                continue
            if k == len(rowLeftToRight)-1:
                count += 1
                # print('reached end of forest')
                # print('final count is', count)  
                countsPerTree[i][j] *= count
                count = 0   
                break
            elif maximum1 == float(rowLeftToRight[i][k]):
                # print(maximum1, 'is equal to', rowLeftToRight[i][k])
                count += 1 
                # print('stop count and go to next tree') 
                # print('final count is', count)
                countsPerTree[i][j] *= count
                count = 0    
                break
            else:
                count += 1
                # print(maximum1, 'is not bigger than', rowLeftToRight[i][k])
                # print('stop count and go to next tree')
                # print('final count is', count)
                countsPerTree[i][j] *= count 
                count = 0   
                break
        
        # look left
        for k in range(-j, 0): #looks at columns from left to right in the forest matrix :p
            # print('looking at column', k, ', maximum is', maximum1)
            if maximum1 > float(rowRightToLeft[i][k]):
                # print(maximum1, 'is bigger than', rowRightToLeft[i][k])
                count += 1
                # print('count is' ,count)
                if k == -1:
                    # print('reached end of forest')
                    # print('final count is', count)
                    countsPerTree[i][j] *= count
                    count = 0    
                    break
                continue
            if k == -1:
                count += 1
                # print('reached end of forest')
                # print('final count is', count)  
                countsPerTree[i][j] *= count  
                count = 0    
                break
            elif maximum1 == float(rowRightToLeft[i][k]):
                # print(maximum1, 'is equal to', rowRightToLeft[i][k])
                count += 1 
                # print('stop count and go to next tree') 
                # print('final count is', count)
                countsPerTree[i][j] *= count 
                count = 0   
                break
            else:
                count += 1
                # print(maximum1, 'is not bigger than', rowRightToLeft[i][k])
                # print('stop count and go to next tree')
                # print('final count is', count)
                countsPerTree[i][j] *= count 
                count = 0   
                break

# to check up and down
for i in range(1,len(columnTopToBottom)-1):
    # print('changing to column', i)
    for j in range(1,len(columnTopToBottom[0])-1):
        # print('changing to row', j)
        maximum1 = forest1[j][i] 
        count = 0
        # look down
        for k in range(j+1,len(columnTopToBottom)):
            # print('looking at row', k, ', maximum is', maximum1)
            if maximum1 > float(columnTopToBottom[i][k]):
                # print(maximum1, 'is bigger than', columnTopToBottom[i][k])
                count += 1
                # print('count is' ,count)
                if k == len(columnTopToBottom)-1:
                    # print('reached end of forest')
                    # print('final count is', count)
                    countsPerTree[j][i] *= count 
                    count = 0
                    break
                continue
            if k == len(columnTopToBottom)-1:
                count += 1
                # print('reached end of forest')
                # print('final count is', count)  
                countsPerTree[j][i] *= count
                count = 0   
                break
            elif maximum1 == float(columnTopToBottom[i][k]):
                # print(maximum1, 'is equal to', columnTopToBottom[i][k])
                count += 1 
                # print('stop count and go to next tree') 
                # print('final count is', count)
                countsPerTree[j][i] *= count
                count = 0    
                break
            else:
                count += 1
                # print(maximum1, 'is not bigger than', columnTopToBottom[i][k])
                # print('stop count and go to next tree')
                # print('final count is', count)
                countsPerTree[j][i] *= count 
                count = 0   
                break
            
        # look up
        for k in range(-j, 0): #looks at rows from down to up in the forest matrix :p
            # print('looking at row', k, ', maximum is', maximum1)
            if maximum1 > float(columnBottomToTop[i][k]):
                # print(maximum1, 'is bigger than', columnBottomToTop[i][k])
                count += 1
                # print('count is' ,count)
                if k == -1:
                    # print('reached end of forest')
                    # print('final count is', count)
                    countsPerTree[j][i] *= count
                    count = 0    
                    break
                continue
            if k == -1:
                count += 1
                # print('reached end of forest')
                # print('final count is', count)  
                countsPerTree[j][i] *= count  
                count = 0    
                break
            elif maximum1 == float(columnBottomToTop[i][k]):
                # print(maximum1, 'is equal to', columnBottomToTop[i][k])
                count += 1 
                # print('stop count and go to next tree') 
                # print('final count is', count)
                countsPerTree[j][i] *= count 
                count = 0   
                break
            else:
                count += 1
                # print(maximum1, 'is not bigger than', columnBottomToTop[i][k])
                # print('stop count and go to next tree')
                # print('final count is', count)
                countsPerTree[j][i] *= count 
                count = 0   
                break
            
# print(countsPerTree)
# print(forest1)

answer2 = countsPerTree.max()
print(answer2)