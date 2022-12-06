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
        if crate and crate != ' ':
            stacks[stack].insert(0, crate)

# Discard the number line and the whitespace line
f.readline()
f.readline()


# Now follow directions
for line in f:
    instructions = line.split(' ')
    from_stack = int(instructions[3]) - 1
    number_to_move = min(int(instructions[1]), len(stacks[from_stack]))
    to_stack = int(instructions[5]) - 1

    if len(stacks[from_stack]) <= 0:
        continue
    crates = stacks[from_stack][-number_to_move:]
    del stacks[from_stack][-number_to_move:]
    stacks[to_stack] += crates

result_string = ''
for i in range(9):
    if len(stacks[i]) == 0:
        result_string += ' '
    else:
        result_string += stacks[i][-1]

print(f"Done. Result string is {result_string}")