List = open("day1.txt").read().splitlines()
Data = []
for i in range(0,len(List)):
    if len(List[i]):
        Data.append(int(List[i]))
    else:
        Data.append(None)

Data.append(None)
finaList = []
toadd = []
for j in range(0,len(Data)):
    if not Data[j] == None:
        toadd.append(Data[j])
    else:
        tosum = sum(toadd)
        finaList.append(tosum)
        toadd = []
        tosum = []
        continue

answer1 = max(finaList)

tosumtoo = []
for k in range(0,3):
    tosumtoo.append(max(finaList))
    finaList.remove(max(finaList))
answer2 = sum(tosumtoo)