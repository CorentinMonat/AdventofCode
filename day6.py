import re
data = open("day6.txt").read()
# data = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
# data = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
# data = 'nppdvjthqldpwncqszvftbrmjlhg'
# data = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
# data = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

# Part 1
for i in range(0,len(data)):  
        if i>=4 and  data[i-1] != data[i-2] and data[i-1]!= data[i-3] and data[i-1] != data[i-4] and data[i-2] != data[i-3] and data[i-2] != data[i-4] and data[i-3] != data[i-4]:
            answer1 = i
            break
        
# Part 2
for i in range(14,len(data)):
    # MOST efficient way to solve this:   (less efficient way below this disasterpiece)  
    if data[i-14] != data[i-13]:
        if data[i-14] != data[i-12]:
            if data[i-14] != data[i-11]:
                if data[i-14] != data[i-10]:
                    if data[i-14] != data[i-9]:
                        if data[i-14] != data[i-8]:
                            if data[i-14] != data[i-7]:
                                if data[i-14] != data[i-6]:
                                    if data[i-14] != data[i-5]:
                                        if data[i-14] != data[i-4]:
                                            if data[i-14] != data[i-3]:
                                                if data[i-14] != data[i-2]:
                                                    if data[i-14] != data[i-1]:
                                                        if data[i-13] != data[i-12]:
                                                            if data[i-13] != data[i-11]:
                                                                if data[i-13] != data[i-10]:
                                                                    if data[i-13] != data[i-9]:
                                                                        if data[i-13] != data[i-8]:
                                                                            if data[i-13] != data[i-7]:
                                                                                if data[i-13] != data[i-6]:
                                                                                    if data[i-13] != data[i-5]:
                                                                                        if data[i-13] != data[i-4]:
                                                                                            if data[i-13] != data[i-3]:
                                                                                                if data[i-13] != data[i-2]:
                                                                                                    if data[i-13] != data[i-1]:
                                                                                                        if data[i-12] != data[i-11]:
                                                                                                            if data[i-12] != data[i-10]:
                                                                                                                if data[i-12] != data[i-9]:
                                                                                                                    if data[i-12] != data[i-8]:
                                                                                                                        if data[i-12] != data[i-7]:
                                                                                                                            if data[i-12] != data[i-6]:
                                                                                                                                if data[i-12] != data[i-5]:
                                                                                                                                    if data[i-12] != data[i-4]:
                                                                                                                                        if data[i-12] != data[i-3]:
                                                                                                                                            if data[i-12] != data[i-2]:
                                                                                                                                                if data[i-12] != data[i-1]:
                                                                                                                                                    if data[i-11] != data[i-10]:
                                                                                                                                                        if data[i-11] != data[i-9]:
                                                                                                                                                            if data[i-11] != data[i-8]:
                                                                                                                                                                if data[i-11] != data[i-7]:
                                                                                                                                                                    if data[i-11] != data[i-6]:
                                                                                                                                                                        if data[i-11] != data[i-5]:
                                                                                                                                                                            if data[i-11] != data[i-4]:
                                                                                                                                                                                if data[i-11] != data[i-3]:
                                                                                                                                                                                    if data[i-11] != data[i-2]:
                                                                                                                                                                                        if data[i-11] != data[i-1]:
                                                                                                                                                                                            if data[i-10] != data[i-9]:
                                                                                                                                                                                                if data[i-10] != data[i-8]:
                                                                                                                                                                                                    if data[i-10] != data[i-7]:
                                                                                                                                                                                                        if data[i-10] != data[i-6]:
                                                                                                                                                                                                            if data[i-10] != data[i-5]:
                                                                                                                                                                                                                if data[i-10] != data[i-4]:
                                                                                                                                                                                                                    if data[i-10] != data[i-3]:
                                                                                                                                                                                                                        if data[i-10] != data[i-2]:
                                                                                                                                                                                                                            if data[i-10] != data[i-1]:
                                                                                                                                                                                                                                if data[i-9] != data[i-8]:
                                                                                                                                                                                                                                    if data[i-9] != data[i-7]:
                                                                                                                                                                                                                                        if data[i-9] != data[i-6]:
                                                                                                                                                                                                                                            if data[i-9] != data[i-5]:
                                                                                                                                                                                                                                                if data[i-9] != data[i-4]:
                                                                                                                                                                                                                                                    if data[i-9] != data[i-3]:
                                                                                                                                                                                                                                                        if data[i-9] != data[i-2]:
                                                                                                                                                                                                                                                            if data[i-9] != data[i-1]:
                                                                                                                                                                                                                                                                if data[i-8] != data[i-7]:
                                                                                                                                                                                                                                                                    if data[i-8] != data[i-6]:
                                                                                                                                                                                                                                                                        if data[i-8] != data[i-5]:
                                                                                                                                                                                                                                                                            if data[i-8] != data[i-4]:
                                                                                                                                                                                                                                                                                if data[i-8] != data[i-3]:
                                                                                                                                                                                                                                                                                    if data[i-8] != data[i-2]:
                                                                                                                                                                                                                                                                                        if data[i-8] != data[i-1]:
                                                                                                                                                                                                                                                                                            if data[i-7] != data[i-6]:
                                                                                                                                                                                                                                                                                                if data[i-7] != data[i-5]:
                                                                                                                                                                                                                                                                                                    if data[i-7] != data[i-4]:
                                                                                                                                                                                                                                                                                                        if data[i-7] != data[i-3]:
                                                                                                                                                                                                                                                                                                            if data[i-7] != data[i-2]:
                                                                                                                                                                                                                                                                                                                if data[i-7] != data[i-1]:
                                                                                                                                                                                                                                                                                                                    if data[i-6] != data[i-5]:
                                                                                                                                                                                                                                                                                                                        if data[i-6] != data[i-4]:
                                                                                                                                                                                                                                                                                                                            if data[i-6] != data[i-3]:
                                                                                                                                                                                                                                                                                                                                if data[i-6] != data[i-2]:
                                                                                                                                                                                                                                                                                                                                    if data[i-6] != data[i-1]:
                                                                                                                                                                                                                                                                                                                                        if data[i-5] != data[i-4]:
                                                                                                                                                                                                                                                                                                                                            if data[i-5] != data[i-3]:
                                                                                                                                                                                                                                                                                                                                                if data[i-5] != data[i-2]:
                                                                                                                                                                                                                                                                                                                                                    if data[i-5] != data[i-1]:
                                                                                                                                                                                                                                                                                                                                                        if data[i-4] != data[i-3]:
                                                                                                                                                                                                                                                                                                                                                            if data[i-4] != data[i-2]:
                                                                                                                                                                                                                                                                                                                                                                if data[i-4] != data[i-1]:
                                                                                                                                                                                                                                                                                                                                                                    if data[i-3] != data[i-2]:
                                                                                                                                                                                                                                                                                                                                                                        if data[i-3] != data[i-1]:
                                                                                                                                                                                                                                                                                                                                                                            if data[i-2] != data[i-1]:
                                                                                                                                                                                                                                                                                                                                                                                print(i)
                                                                                                                                                                                                                                                                                                                                                                                break

# Much better way:
n = 0
for i in range(len(data)-14):
    for j in range(14):
        marker = r'[^'+data[i+j+1:i+15]+']'
        if re.match(marker,data[i+j]):
            n += 1
        else:
            n = 0
            continue
    if n == 13:
        answer2 = i + 15
        break
    n = 0
print(answer2)