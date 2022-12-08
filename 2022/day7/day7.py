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

dir_structure = {}
current_dir_stack = [dir_structure]

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

all_directories = []
addContainingDirs(dir_structure, all_directories)

total_total = 0
for dir in all_directories:
    size = countDir(dir)
    if size <= 100000:
        total_total += size

print(f"done: {total_total}")