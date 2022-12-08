import re
# data = open("day7.txt").read().splitlines()
data = ['$ cd /', '$ ls', 'dir a', '14848514 b.txt', '8504156 c.dat', 'dir d', '$ cd a', '$ ls', 'dir e', '29116 f', '2557 g', '62596 h.lst', '$ cd e', '$ ls', '584 i', '$ cd ..', '$ cd ..', '$ cd d', '$ ls', '4060174 j', '8033020 d.log', '5626152 d.ext', '7214296 k']

# Make class to have one list per path to a folder
class Stack():
    
    def __init__(self):
        self.path = []
    
    def push(self, item):
        self.path.append(item)
        
    def pop(self):
        if len(self.path):
            self.path.pop()
        else:
            return None    
    
# Find how many folders there are. (to later fill lists with each folder's path)
numberOfFolders = 1
for i in range(len(data)):
    if "dir" in data[i]:
        numberOfFolders += 1
       
folderPaths = [[]] * numberOfFolders
# Find path of each folder
for j in range(0,numberOfFolders):
    folderPaths[j] = Stack()
    n = 0
    for i in range(0,len(data)):
        if "$ cd " in data[i]:
            folderPaths[j].push(data[i])
            # print('adding', folderPaths[j].path[-1])
            n += 1
            
        if "$ cd .." in data[i]:
            # print('removing', folderPaths[j].path[-1])
            folderPaths[j].pop()
            # print('removing', folderPaths[j].path[-1])
            folderPaths[j].pop()
            n -= 1
        
        if n == j+1:
            # print(n)
            # print('going to next folder path')
            break    
    print(folderPaths[j].path)    
        
# Find how many files there are
numberOfFiles = 0
# if there is an integer in str, it is a file
for i in range(0,len(data)):
    if len([int(s) for s in re.findall(r'\b\d+\b', data[i])]):
        numberOfFiles += 1
        
# Find path of each file
# count how many elements between each cd, then you know what is in each folder
filePaths = [[]] * numberOfFiles
for j in range(0,1):
    filePaths[j] = Stack()
    m = 0
    for i in range(0,len(data)):
        if "cd" in data[i]:
            filePaths[j].push(data[i])