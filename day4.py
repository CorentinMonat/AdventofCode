import re
List = open("day4.txt").read().splitlines()
# List = ['2-4,6-8','2-3,4-5','5-7,7-9','2-8,3-7','6-6,4-6','2-6,4-8'] 

fullyContained = []
for i in range(0,len(List)):
    a = [int(s) for s in re.findall(r'\b\d+\b', List[i])]
    if a[0] >= a[2] and a[1] <= a[3]:
        fullyContained.append(1)
    elif a[0] <= a[2] and a[1] >= a[3]:
        fullyContained.append(1)
answer1 = sum(fullyContained)

partlyContained = []
for elem in range(0,len(List)):
    b = [int(s) for s in re.findall(r'\b\d+\b', List[elem])]
    if  b[2] <= b[1] and b[3] >= b[0]:
        partlyContained.append(1)
      
answer2 = sum(partlyContained)