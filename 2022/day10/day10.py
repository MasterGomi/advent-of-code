f = open(r"2022\day10\day10input.txt")

register_val = 1
program_counter = 0
cycles = 1
instructions = f.readlines()
targets = [20, 60, 100, 140, 180, 220]
wait = False
total = 0

while program_counter < len(instructions):
    if cycles in targets:
        total += register_val * cycles
    cycles += 1
    if wait:
        wait = False
        to_add = int(instruction[5:])
        register_val += to_add
        program_counter += 1
        continue
    instruction = instructions[program_counter]
    if instruction[:4] == "addx":
        wait = True
    else:
        program_counter += 1

print(f"Total across targets: {str(total)}")