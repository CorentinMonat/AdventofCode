import re
data = open("day5.txt").read().splitlines()
#         [J]         [B]     [T]    
#         [M] [L]     [Q] [L] [R]    
#         [G] [Q]     [W] [S] [B] [L]
# [D]     [D] [T]     [M] [G] [V] [P]
# [T]     [N] [N] [N] [D] [J] [G] [N]
# [W] [H] [H] [S] [C] [N] [R] [W] [D]
# [N] [P] [P] [W] [H] [H] [B] [N] [G]
# [L] [C] [W] [C] [P] [T] [M] [Z] [W]
#  1   2   3   4   5   6   7   8   9 
one = ['L','N','W','T','D']
two = ['C','P','H']
three = ['W','P','H','N','D','G','M','J']
four = ['C','W','S','N','T','Q','L']
five = ['P','H','C','N']
six = ['T','H','N','D','M','W','Q','B']
seven = ['M','B','R','J','G','S','L']
eight = ['Z','N','W','G','V','B','R','T']
nine = ['W','G','D','N','P','L']



# one = ['Z','N']
# two = ['M','C','D']
# three = ['P']
# data = ['move 1 from 2 to 1','move 3 from 1 to 3','move 2 from 2 to 1','move 1 from 1 to 2']

howMany = []
fromWhere = []
toWhere = []
for i in range(0,len(data)):
    a = [int(s) for s in re.findall(r'\b\d+\b', data[i])]
    howMany.append(a[0])
    fromWhere.append(a[1])
    toWhere.append(a[2])
    
# Part 1
# for k in range(0,len(howMany)):
#     if fromWhere[k] == 1:
#         fromWhere[k] = one
#     if fromWhere[k] == 2:
#         fromWhere[k] = two
#     if fromWhere[k] == 3:
#         fromWhere[k] = three  
#     # if fromWhere[k] == 4:
#     #     fromWhere[k] = four
#     # if fromWhere[k] == 5:
#     #     fromWhere[k] = five
#     # if fromWhere[k] == 6:
#     #     fromWhere[k] = six  
#     # if fromWhere[k] == 7:
#     #     fromWhere[k] = seven
#     # if fromWhere[k] == 8:
#     #     fromWhere[k] = eight
#     # if fromWhere[k] == 9:
#     #     fromWhere[k] = nine    
        
#     if toWhere[k] == 1:
#         toWhere[k] = one
#     if toWhere[k] == 2:
#         toWhere[k] = two
#     if toWhere[k] == 3:
#         toWhere[k] = three  
#     # if toWhere[k] == 4:
#     #     toWhere[k] = four
#     # if toWhere[k] == 5:
#     #     toWhere[k] = five
#     # if toWhere[k] == 6:
#     #     toWhere[k] = six 
#     # if toWhere[k] == 7:
#     #     toWhere[k] = seven
#     # if toWhere[k] == 8:
#     #     toWhere[k] = eight
#     # if toWhere[k] == 9:
#     #     toWhere[k] = nine 
        
        
#     for j in range(0,howMany[k]):
#         removed = fromWhere[k].pop()
#         toWhere[k].append(removed)

# Answer Part 1 :D
# print(one)
# print(two)
# print(three)
# print(four)
# print(five)
# print(six)
# print(seven)
# print(eight)
# print(nine)

# Part 2

for k in range(0,len(howMany)):
    if fromWhere[k] == 1:
        fromWhere[k] = one
    if fromWhere[k] == 2:
        fromWhere[k] = two
    if fromWhere[k] == 3:
        fromWhere[k] = three  
    if fromWhere[k] == 4:
        fromWhere[k] = four
    if fromWhere[k] == 5:
        fromWhere[k] = five
    if fromWhere[k] == 6:
        fromWhere[k] = six  
    if fromWhere[k] == 7:
        fromWhere[k] = seven
    if fromWhere[k] == 8:
        fromWhere[k] = eight
    if fromWhere[k] == 9:
        fromWhere[k] = nine    
        
    if toWhere[k] == 1:
        toWhere[k] = one
    if toWhere[k] == 2:
        toWhere[k] = two
    if toWhere[k] == 3:
        toWhere[k] = three  
    if toWhere[k] == 4:
        toWhere[k] = four
    if toWhere[k] == 5:
        toWhere[k] = five
    if toWhere[k] == 6:
        toWhere[k] = six 
    if toWhere[k] == 7:
        toWhere[k] = seven
    if toWhere[k] == 8:
        toWhere[k] = eight
    if toWhere[k] == 9:
        toWhere[k] = nine 
    for j in range(howMany[k],0,-1):
        # print(one)
        # print(two)
        # print(three)
        removed = fromWhere[k].pop(-j)
        toWhere[k].append(removed)
        # print('Next round')
        
# Answer Part 2
print(one)
print(two)
print(three)
print(four)
print(five)
print(six)
print(seven)
print(eight)
print(nine)