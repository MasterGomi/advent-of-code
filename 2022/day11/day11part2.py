import math

f = open(r"2022\day11\day11simplifiedInput.txt")

ROUNDS = 10000

# We're going to have to hard-code a lot of this for time
def monkey0Operation(input):
    return input * 19

def monkey1Operation(input):
    return input + 1

def monkey2Operation(input):
    return input + 6

def monkey3Operation(input):
    return input + 5

def monkey4Operation(input):
    return input * input

def monkey5Operation(input):
    return input + 7

def monkey6Operation(input):
    return input * 7

def monkey7Operation(input):
    return input + 2

def monkey0PassesTo(input):
    test = input % 7 == 0
    if test:
        return 2
    else: 
        return 3

def monkey1PassesTo(input):
    test = input % 19 == 0
    if test:
        return 4
    else: 
        return 6

def monkey2PassesTo(input):
    test = input % 5 == 0
    if test:
        return 7
    else: 
        return 5

def monkey3PassesTo(input):
    test = input % 11 == 0
    if test:
        return 5
    else: 
        return 2

def monkey4PassesTo(input):
    test = input % 17 == 0
    if test:
        return 0
    else: 
        return 3

def monkey5PassesTo(input):
    test = input % 13 == 0
    if test:
        return 1
    else: 
        return 7

def monkey6PassesTo(input):
    test = input % 2 == 0
    if test:
        return 0
    else: 
        return 4

def monkey7PassesTo(input):
    test = input % 3 == 0
    if test:
        return 1
    else: 
        return 6

MONKEY_OPERATIONS = [
    monkey0Operation, 
    monkey1Operation,
    monkey2Operation,
    monkey3Operation,
    monkey4Operation,
    monkey5Operation,
    monkey6Operation,
    monkey7Operation
]

MONKEY_PASSES_TO = [
    monkey0PassesTo, 
    monkey1PassesTo,
    monkey2PassesTo,
    monkey3PassesTo,
    monkey4PassesTo,
    monkey5PassesTo,
    monkey6PassesTo,
    monkey7PassesTo
]

monkey_inventories = []
monkey_inspects = [0] * 8

lines = f.readlines()
for i in range(len(lines)):
    line = lines[i]
    # I love list interpolation sooo much. Glad I can use it
    monkey_inventories.append([int(x.strip()) for x in line.split(',')])

for round in range(ROUNDS):
    print(f"Round {str(round)}")
    for monkey in range(8):
        while monkey_inventories[monkey]:
            item = monkey_inventories[monkey][0]
            processed_item = MONKEY_OPERATIONS[monkey](item)
            passes_to = MONKEY_PASSES_TO[monkey](processed_item)
            monkey_inventories[passes_to].append(processed_item)
            del monkey_inventories[monkey][0]
            monkey_inspects[monkey] += 1

monkey_inspects.sort(reverse=True)
monkey_business = monkey_inspects[0] * monkey_inspects[1]

print(f"Monkey business is: {monkey_business}")