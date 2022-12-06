f = open(r"2022\day5\day5input.txt")

# Array of nine empty lists
# Obviously I'm relying on there being 9 here, because making a generic approach sound like effort
stacks = [[],[],[],[],[],[],[],[],[]]

for i in range(8):
    # these are the lines that define the stacks' starting state
    line = f.readline()
    offset = 1
    inbetween = 4
    for stack in range(9):
        k = offset + (inbetween * stack)
        crate = line[k]
        if crate and crate is not ' ':
            stacks[stack].insert(0, crate)

# Discard the number line and the whitespace line
f.readline()
f.readline()


# Now follow directions
for line in f:
    instructions = line.split(' ')
    number_to_move = int(instructions[1])
    from_stack = int(instructions[3]) - 1
    to_stack = int(instructions[5]) - 1

    for x in range(number_to_move):
        if len(stacks[from_stack]) <= 0:
            continue
        crate = stacks[from_stack].pop()
        stacks[to_stack].append(crate)

result_string = ''
for i in range(9):
    result_string += stacks[i][-1]

print(f"Done. Result string is {result_string}")