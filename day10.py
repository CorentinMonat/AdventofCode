import numpy as np
np.set_printoptions(linewidth=np.inf)
data = open("day10.txt").read().splitlines()

# Part 1
# X starts with value 1, and number of cycles is 0 at first
X = 1
count = 0
strength = []
for i in range(len(data)):
    # if line starts with noop, add one cycle, X does not change
    if "noop" in data[i]:
        count += 1 
        # print('noop is called, count is', count, 'and X is', X)        
        if count == 19 or count == 59 or count == 99 or count == 139 or count == 179 or count == 219:
            strength.append(X*(count+1))
            
    
    #if line starts with addx, cycle increases by 2, add value after 'addx' to X after the second cycle!!
    if "addx" in data[i]:
        count += 1
        # print('first cycle of addx, count is', count, 'and X is still', X)
        if count == 19 or count == 59 or count == 99 or count == 139 or count == 179 or count == 219:
            strength.append(X*(count+1))
        count +=1
        X += int(data[i].split(" ")[1])
        # print('second cycle of addx, count is', count, 'and X is now', X)
        if count == 19 or count == 59 or count == 99 or count == 139 or count == 179 or count == 219:
            strength.append(X*(count+1))
            
answer1 = sum(strength)
print("answer 1 is", answer1)

# Part 2 

# number the columns of the sprite (each letter is 5 columns)
# a = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]
# print(a)

# X goes fom -1 to 39, and starts at 1 
X = 1
count = 0
CPU = np.ones((6,40), dtype=None)
sprite = [0]*40
sprite[X-1] = 1
sprite[X] = 1
sprite[X+1] = 1
# print(sprite)
spritecount = 1

for i in range(len(data)):
    
    #if line starts with noop, add one cycle, X does not change
    if "noop" in data[i]:
        # add 0 or leave 1 to CPU pixel for the first row
        if count < 40:
            if sprite[count] == 1:
                # print('count is',count)
                # print('sprite is', sprite)
                # print('so',sprite[count],'is equal to 1')
                CPU[0,count] = 0
            #     print('updated CPU is', CPU)
            # else:
            #     print(sprite[count], 'is not 1, so CPU pixel does not change at pixel', count)
                
        # add 0 or leave 1 to CPU pixel for the second row
        if count >= 40 and count < 80:
            if sprite[count-40] == 1:
                # print('count is',count)
                # print('sprite is', sprite)
                # print('so',sprite[count-40],'is equal to 1')
                CPU[1,count-40] = 0
            #     print('updated CPU is', CPU)
            # else:
            #     print(sprite[count-40], 'is not 1, so CPU pixel does not change at pixel', count)
                
        # add 0 or leave 1 to CPU pixel for the third row
        if count >= 80 and count < 120:
            if sprite[count-80] == 1:
                # print('count is',count)
                # print('sprite is', sprite)
                # print('so',sprite[count-80],'is equal to 1')
                CPU[2,count-80] = 0
            #     print('updated CPU is', CPU)
            # else:
            #     print(sprite[count-80], 'is not 1, so CPU pixel does not change at pixel', count)
                
        # add 0 or leave 1 to CPU pixel for the fourth row
        if count >= 120 and count < 160:
            if sprite[count-120] == 1:
                # print('count is',count)
                # print('sprite is', sprite)
                # print('so',sprite[count-120],'is equal to 1')
                CPU[3,count-120] = 0
            #     print('updated CPU is', CPU)
            # else:
            #     print(sprite[count-120], 'is not 1, so CPU pixel does not change at pixel', count)
                
        # add 0 or leave 1 to CPU pixel for the fifth row
        if count >= 160 and count < 200:
            if sprite[count-160] == 1:
                # print('count is',count)
                # print('sprite is', sprite)
                # print('so',sprite[count-160],'is equal to 1')
                CPU[4,count-160] = 0
            #     print('updated CPU is', CPU)
            # else:
            #     print(sprite[count-160], 'is not 1, so CPU pixel does not change at pixel', count)
                
        # add 0 or leave 1 to CPU pixel for the sixth row
        if count >= 200 and count < 240:
            if sprite[count-200] == 1:
                # print('count is',count)
                # print('sprite is', sprite)
                # print('so',sprite[count-200],'is equal to 1')
                CPU[5,count-200] = 0
            #     print('updated CPU is', CPU)
            # else:
            #     print(sprite[count-200], 'is not 1, so CPU pixel does not change at pixel', count)
        count += 1        

    #if line starts with addx, cycle increases by 2, add value after 'addx' to X after the second cycle!!
    if "addx" in data[i]:
        # add 0 or leave 1 to CPU pixel for the first row
        if count < 40:
            if sprite[count] == 1:
                # print('count is',count)
                # print('sprite is', sprite)
                # print('so',sprite[count],'is equal to 1')
                CPU[0,count] = 0
            #     print('updated CPU is', CPU)
            # else:
            #     print(sprite[count], 'is not 1, so CPU pixel does not change at pixel', count)
                
        # add 0 or leave 1 to CPU pixel for the second row
        if count >= 40 and count < 80:
            if sprite[count-40] == 1:
                # print('count is',count)
                # print('sprite is', sprite)
                # print('so',sprite[count-40],'is equal to 1')
                CPU[1,count-40] = 0
            #     print('updated CPU is', CPU)
            # else:
            #     print(sprite[count-40], 'is not 1, so CPU pixel does not change at pixel', count)
                
        # add 0 or leave 1 to CPU pixel for the third row
        if count >= 80 and count < 120:
            if sprite[count-80] == 1:
                # print('count is',count)
                # print('sprite is', sprite)
                # print('so',sprite[count-80],'is equal to 1')
                CPU[2,count-80] = 0
            #     print('updated CPU is', CPU)
            # else:
            #     print(sprite[count-80], 'is not 1, so CPU pixel does not change at pixel', count)
                
        # add 0 or leave 1 to CPU pixel for the fourth row
        if count >= 120 and count < 160:
            if sprite[count-120] == 1:
                # print('count is',count)
                # print('sprite is', sprite)
                # print('so',sprite[count-120],'is equal to 1')
                CPU[3,count-120] = 0
            #     print('updated CPU is', CPU)
            # else:
            #     print(sprite[count-120], 'is not 1, so CPU pixel does not change at pixel', count)
                
        # add 0 or leave 1 to CPU pixel for the fifth row
        if count >= 160 and count < 200:
            if sprite[count-160] == 1:
                # print('count is',count)
                # print('sprite is', sprite)
                # print('so',sprite[count-160],'is equal to 1')
                CPU[4,count-160] = 0
            #     print('updated CPU is', CPU)
            # else:
            #     print(sprite[count-160], 'is not 1, so CPU pixel does not change at pixel', count)
                
        # add 0 or leave 1 to CPU pixel for the sixth row
        if count >= 200 and count < 240:
            if sprite[count-200] == 1:
                # print('count is',count)
                # print('sprite is', sprite)
                # print('so',sprite[count-200],'is equal to 1')
                CPU[5,count-200] = 0
            #     print('updated CPU is', CPU)
            # else:
            #     print(sprite[count-200], 'is not 1, so CPU pixel does not change at pixel', count)
                
        count +=1
        
        # add 0 or leave 1 to CPU pixel for the first row
        if count < 40:
            if sprite[count] == 1:
                # print('count is',count)
                # print('sprite is', sprite)
                # print('so',sprite[count],'is equal to 1')
                CPU[0,count] = 0
            #     print('updated CPU is', CPU)
            # else:
            #     print(sprite[count], 'is not 1, so CPU pixel does not change at pixel', count)
                
        # add 0 or leave 1 to CPU pixel for the second row
        if count >= 40 and count < 80:
            if sprite[count-40] == 1:
                # print('count is',count)
                # print('sprite is', sprite)
                # print('so',sprite[count-40],'is equal to 1')
                CPU[1,count-40] = 0
            #     print('updated CPU is', CPU)
            # else:
            #     print(sprite[count-40], 'is not 1, so CPU pixel does not change at pixel', count)
                
        # add 0 or leave 1 to CPU pixel for the third row
        if count >= 80 and count < 120:
            if sprite[count-80] == 1:
                # print('count is',count)
                # print('sprite is', sprite)
                # print('so',sprite[count-80],'is equal to 1')
                CPU[2,count-80] = 0
            #     print('updated CPU is', CPU)
            # else:
            #     print(sprite[count-80], 'is not 1, so CPU pixel does not change at pixel', count)
                
        # add 0 or leave 1 to CPU pixel for the fourth row
        if count >= 120 and count < 160:
            if sprite[count-120] == 1:
                # print('count is',count)
                # print('sprite is', sprite)
                # print('so',sprite[count-120],'is equal to 1')
                CPU[3,count-120] = 0
            #     print('updated CPU is', CPU)
            # else:
            #     print(sprite[count-120], 'is not 1, so CPU pixel does not change at pixel', count)
                
        # add 0 or leave 1 to CPU pixel for the fifth row
        if count >= 160 and count < 200:
            if sprite[count-160] == 1:
                # print('count is',count)
                # print('sprite is', sprite)
                # print('so',sprite[count-160],'is equal to 1')
                CPU[4,count-160] = 0
            #     print('updated CPU is', CPU)
            # else:
            #     print(sprite[count-160], 'is not 1, so CPU pixel does not change at pixel', count)
                
        # add 0 or leave 1 to CPU pixel for the sixth row
        if count >= 200 and count < 240:
            if sprite[count-200] == 1:
                # print('count is',count)
                # print('sprite is', sprite)
                # print('so',sprite[count-200],'is equal to 1')
                CPU[5,count-200] = 0
                # print('updated CPU is', CPU)
            # else:
                # print(sprite[count-200], 'is not 1, so CPU pixel does not change at pixel', count)
                
        count += 1

        X += int(data[i].split(" ")[1])
        if X == -1:
            sprite = [0]*40
            sprite[X+1] = 1
        elif X == 0:
            sprite = [0]*40
            sprite[X] = 1
            sprite[X+1] = 1
        elif X == 39:
            sprite = [0]*40
            sprite[X] = 1
            sprite[X-1] = 1
        else:
            sprite = [0]*40
            sprite[X-1] = 1
            sprite[X] = 1
            sprite[X+1] = 1
        # print(sprite)


# print(CPU)
print('answer 2 is ERCREPCJ')
    
    

