f = open(r"2022\day9\day9input.txt")

h_x = 0
h_y = 0
t_x = 0
t_y = 0

vistited = {}

for line in f:
    vistited[(t_x, t_y)] = True

    # Get movement details
    direction = line[0]
    distance = int(line[2:])

    # Move head
    # The extra adjustment accounts for diagonal movement
    if direction == 'U':
        h_y += distance
        if h_y - t_y >= 2:
            if t_x > h_x:
                t_x -= 1
            elif t_x < h_x:
                t_x += 1
    elif direction == 'D':
        h_y -= distance
        if h_y - t_y <= -2:
            if t_x > h_x:
                t_x -= 1
            elif t_x < h_x:
                t_x += 1
    elif direction == 'R':
        h_x += distance
        if h_x - t_x >= 2:
            if t_y > h_y:
                t_y -= 1
            elif t_y < h_y:
                t_y += 1
    elif direction == 'L':
        h_x -= distance
        if h_x - t_x <= -2:
            if t_y > h_y:
                t_y -= 1
            elif t_y < h_y:
                t_y += 1
    
    while t_y < h_y - 1:
        t_y += 1
        vistited[(t_x, t_y)] = True
    while t_y > h_y + 1:
        t_y -= 1
        vistited[(t_x, t_y)] = True
    while t_x < h_x - 1:
        t_x += 1
        vistited[(t_x, t_y)] = True
    while t_x > h_x + 1:
        t_x -= 1
        vistited[(t_x, t_y)] = True

print(f"Done. Tail visted {str(len(vistited.keys()))} spaces")