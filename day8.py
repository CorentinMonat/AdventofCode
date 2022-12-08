import re
# data = open("day8.txt").read().splitlines()
data = ['30373', '25512', '65332', '33549', '35390']

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
    
    
# Look at list of numbers from left to right, set first one as max. If next number is higher, count += 1 AND set that number as the new max! 
# Go through the whole list. Then do the same for the other three lists 
# (exact same code because they will also be lists of numbers from left to right)

count = len(rowLeftToRight) + len(rowRightToLeft) + len(columnBottomToTop) + len(columnTopToBottom) - 4
# print('Looking from LEFT to RIGHT')
for i in range(1,len(rowLeftToRight)-1):
    maximum = rowLeftToRight[i][0]
    # print('New row! Maximum is now', maximum)
    for j in range(1,len(rowLeftToRight[i])-1):
        if rowLeftToRight[i][j] > maximum:
            # print(rowLeftToRight[i][j], 'is bigger than', maximum)
            count += 1
            # print('count is ', count)
            maximum = rowLeftToRight[i][j] 
            # print('setting new maximum to', maximum)

# print('Looking from RIGHT to LEFT')
for i in range(1,len(rowRightToLeft)-1):
    maximum = rowRightToLeft[i][0]
    # print('New row! Maximum is now', maximum)
    for j in range(1,len(rowRightToLeft[i])-1):
        if rowRightToLeft[i][j] > maximum:
            # print(rowRightToLeft[i][j], 'is bigger than', maximum)
            count += 1
            # print('count is ', count)
            maximum = rowRightToLeft[i][j] 
            # print('setting new maximum to', maximum)
            
# print('Looking from TOP to BOTTOM')
for i in range(1,len(columnTopToBottom)-1):
    maximum = columnTopToBottom[i][0]
    # print('New column! Maximum is now', maximum)
    for j in range(1,len(columnTopToBottom[i])-1):
        if columnTopToBottom[i][j] > maximum:
            # print(columnTopToBottom[i][j], 'is bigger than', maximum)
            count += 1
            # print('count is ', count)
            maximum = columnTopToBottom[i][j] 
            # print('setting new maximum to', maximum)
        
# print('Looking from BOTTOM to TOP')
for i in range(1,len(columnBottomToTop)-1):
    maximum = columnBottomToTop[i][0]
    # print('New column! Maximum is now', maximum)
    for j in range(1,len(columnBottomToTop[i])-1):
        if columnBottomToTop[i][j] > maximum:
            # print(columnBottomToTop[i][j], 'is bigger than', maximum)
            count += 1
            # print('count is ', count)
            maximum = columnBottomToTop[i][j] 
            # print('setting new maximum to', maximum)
            
# Find duplicates and remove them from count!
# If number is counted from left to right AND number is counted from top to bottom, 
# Then, remove 1 from count

# If number is counted from left to right AND number is counted from right to left, 
# Then, remove 1 from count

# If number is counted from left to right AND number is counted from bottom to top, 
# Then, remove 1 from count

# If number is counted from top to bottom AND number is counted from right to left, 
# Then, remove 1 from count

# If number is counted from top to bottom AND number is counted from bottom to top, 
# Then, remove 1 from count

# If number is counted from right to left AND number is counted from bottom to top, 
# Then, remove 1 from count