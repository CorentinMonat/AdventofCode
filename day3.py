List = open("day3.txt").read().splitlines()
# List = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg', 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']

# Part One
wrongItems = []
# To find wrongly placed items
for elements in range(0,len(List)):
    firstHalf = slice(0, len(List[elements])//2)
    secondHalf = slice(len(List[elements])//2,len(List[elements]))

    # To find which letter is in both strings
    for i in range(0,len(List[elements])//2):
        for j in range(0, len(List[elements])//2):
            if List[elements][firstHalf][i] == List[elements][secondHalf][j]:
                wrongItems.append(List[elements][firstHalf][i])
                break
            else:
                continue
            
        if len(wrongItems) == elements+1 :
            break
        
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphadict = {A: idx+1 for idx, A in enumerate(alphabet)}

# find priority value of each wrong item
priorityValues = []
for k in range(0,len(wrongItems)):
    priorityValues.append(alphadict[wrongItems[k]])
    
answer1 = sum(priorityValues)


# Part Two
commonItems = []
for l in range(0,len(List),3):
    for n in range(0,len(List[l])):
        for m in range(0,len(List[l+1])):
            for o in range(0,len(List[l+2])):
                if List[l][n] == List[l+1][m] and List[l][n] == List[l+2][o]:
                    commonItems.append(List[l][n])
                    print('appending number')
                    break
                else:
                    continue
            if len(commonItems) == (l/3)+1 :
                print(len(commonItems),(l/3)+1)
                break
            
        if len(commonItems) == (l/3)+1 :
            print(len(commonItems),(l/3)+1)
            break
    
    
priorityValues2 = []
for p in range(0,len(commonItems)):
    priorityValues2.append(alphadict[commonItems[p]])
    
answer2 = sum(priorityValues2)