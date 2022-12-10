f = open(r"2022\day10\day10input.txt")

register_val = 1
program_counter = 0
cycles = 0
instructions = f.readlines()
wait = False
display = []

## flow needs to be:
# inc cycle
# draw as visible
# process current command

while program_counter < len(instructions):
    cycles += 1

    # Where are we drawing?
    line = 0
    pos = int(cycles)
    while pos > 40:
        line += 1
        pos -= 40 

    # Add a new line if required
    if pos == 1:
        display.append("")

    # Determine if visible
    visible = register_val <= pos <= register_val + 2

    # Add char to line
    display[line] += '#' if visible else '.'

    # do the command processing
    instruction = instructions[program_counter]
    if wait:
        wait = False
        to_add = int(instruction[5:])
        register_val += to_add
        program_counter += 1
        continue
    if instruction[:4] == "addx":
        wait = True
    else:
        # NOP
        program_counter += 1

print("Done")
for line in display:
    print(line)