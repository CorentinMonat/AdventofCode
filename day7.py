import os
data = open("day7.txt").read().splitlines()
# data = ['$ cd /', '$ ls', 'dir a', '14848514 b.txt', '8504156 c.dat', 'dir d', '$ cd a', '$ ls', 'dir e', '29116 f', '2557 g', '62596 h.lst', '$ cd e', '$ ls', '584 i', '$ cd ..', '$ cd ..', '$ cd d', '$ ls', '4060174 j', '8033020 d.log', '5626152 d.ext', '7214296 k']

# Part 1
current_path = "/"
folders_with_files = {}
# Find path of each folder, and add files and directories of each folder
for line in data:
    if "$ cd " in line:
        current_path = os.path.realpath(os.path.join(current_path, line[4:].strip()))
        if not current_path in folders_with_files:
            folders_with_files[current_path] = {'files' : [], 'directories' : []}
    elif "dir" in line:
        folders_with_files[current_path]['directories'].append(line[4:].strip())
            
    elif line[0] in "0123456789":
        size, name = line.split()
        folders_with_files[current_path]['files'].append([int(size), name])

# directories = {directory: 1 for directory in folders_with_files}
def get_directory_size(folders_with_files, directory):
    files = folders_with_files[directory]['files']
    subdir = folders_with_files[directory]['directories']
    
    sum_files = sum(file[0] for file in files)
    sum_subdir = sum([get_directory_size(folders_with_files, os.path.join(directory, subdirect)) for subdirect in subdir])
    
    return sum_files + sum_subdir


size_of_each_dir = {dirs: get_directory_size(folders_with_files, dirs) for dirs in folders_with_files}

part1 = []
for d in size_of_each_dir:
    if size_of_each_dir[d] < 100000:
        part1.append(size_of_each_dir[d])

answer1 = sum(part1)
print(answer1)

# Part 2
needed_space = 41035571 - 40000000
answer2 = min([size_of_each_dir[d] for d in size_of_each_dir if needed_space < size_of_each_dir[d]])
print(answer2)

