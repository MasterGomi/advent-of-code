# Oh boy, I hope you like recursion

TOTAL_DISK_SPACE = 70000000
REQUIRED_SPACE = 30000000

f = open(r"2022\day7\day7input.txt")

def readDir(current_dir, input):
    '''Takes in a "dir dir_name" line and creates a directory in the dir_structure'''
    dir_name = input[4:]
    current_dir[dir_name] = {}

def readFile(current_dir, input):
    '''Takes in a "123 file.ext" line and adds it to the current directory as {name: size}'''
    details = input.split(' ')
    current_dir[details[1]] = int(details[0])

# ignore the first two lines, as it just establishes that we are in root and lists teh content
f.readline()
f.readline()

# represent the root dir
root_dir = {}
current_dir_stack = [root_dir]

for line in f:
    line = line.strip()
    current_dir = current_dir_stack[-1]
    if line[0] == '$':
        # Command line
        if line == '$ cd ..':
            current_dir_stack.pop()
        elif line == '$ ls':
            continue
        else:
            dir_name = line[5:]
            current_dir_stack.append(current_dir[dir_name])
    
    elif line[:3] == 'dir':
        readDir(current_dir, line)
    else:
        readFile(current_dir, line)

##
##

def countDir(dir):
    total = 0
    for contents in dir.values():
        if not isinstance(contents, int):
            total += countDir(contents)
        else:
            total += contents
    return total

def addContainingDirs(dir, dir_list):
    for x in dir.values():
        if not isinstance(x, int):
            dir_list.append(x)
            addContainingDirs(x, dir_list)

# Get a list of all the dirs in the root dir at every level
all_directories = []
addContainingDirs(root_dir, all_directories)

# How much space is being used?
used_space = countDir(root_dir)

# How much to we need to free?
need_to_free = REQUIRED_SPACE - (TOTAL_DISK_SPACE - used_space)

# What's the smallest directory to delete then?
smallest_suitable = REQUIRED_SPACE
for dir in all_directories:
    size = countDir(dir)
    if size < need_to_free or size > smallest_suitable:
        continue
    smallest_suitable = size

print(f"done. {smallest_suitable}")
