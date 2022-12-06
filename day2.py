List = open("day2.txt").read().splitlines()
# List = ['A Y', 'B X', 'C Z']
# A and X = Rock
# B and Y = Paper
# C and Z = Scissors
# X = 1pt, Y = 2pts, Z = 3pts
# win = 6pt, Draw = 3pts, Lose = 0pt
FinaList = []
for i in range(0,len(List)): 
    if List[i] == 'A X':
        FinaList.append(1+3)
    if List[i] == 'A Y':
        FinaList.append(2+6)
    if List[i] == 'A Z':
        FinaList.append(3+0)
    if List[i] == 'B X':
        FinaList.append(1+0)
    if List[i] == 'B Y':
        FinaList.append(2+3)
    if List[i] == 'B Z':
        FinaList.append(3+6)
    if List[i] == 'C X':
        FinaList.append(1+6)
    if List[i] == 'C Y':
        FinaList.append(2+0)
    if List[i] == 'C Z':
        FinaList.append(3+3)

answer1 = sum(FinaList)


# X = 0pts, Y = 3pts, Z = 6pts
# A = Rock (1pt)
# B = Paper (2pts)
# C = Scissors (3pts)
FinaList2 = []
for i in range(0,len(List)): 
    if List[i] == 'A X':
        FinaList2.append(3+0)
    if List[i] == 'A Y':
        FinaList2.append(1+3)
    if List[i] == 'A Z':
        FinaList2.append(2+6)
    if List[i] == 'B X':
        FinaList2.append(1+0)
    if List[i] == 'B Y':
        FinaList2.append(2+3)
    if List[i] == 'B Z':
        FinaList2.append(3+6)
    if List[i] == 'C X':
        FinaList2.append(2+0)
    if List[i] == 'C Y':
        FinaList2.append(3+3)
    if List[i] == 'C Z':
        FinaList2.append(1+6)
answer2 = sum(FinaList2)