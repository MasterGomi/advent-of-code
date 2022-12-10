f = open(r"2022\day9\day9part2testInput.txt")

def processMovement(head, tail, is_last):
    h_x, h_y = head
    t_x, t_y = tail

    if h_y - t_y >= 2:
        if t_x > h_x:
            t_x -= 1
        elif t_x < h_x:
            t_x += 1
    if h_y - t_y <= -2:
        if t_x > h_x:
            t_x -= 1
        elif t_x < h_x:
            t_x += 1
    if h_x - t_x >= 2:
        if t_y > h_y:
            t_y -= 1
        elif t_y < h_y:
            t_y += 1
    if h_x - t_x <= -2:
        if t_y > h_y:
            t_y -= 1
        elif t_y < h_y:
            t_y += 1
    
    if is_last:
        vistited[(t_x, t_y)] = True

    while t_y < h_y - 1:
        t_y += 1
        if is_last:
            vistited[(t_x, t_y)] = True
    while t_y > h_y + 1:
        t_y -= 1
        if is_last:
            vistited[(t_x, t_y)] = True
    while t_x < h_x - 1:
        t_x += 1
        if is_last:
            vistited[(t_x, t_y)] = True
    while t_x > h_x + 1:
        t_x -= 1
        if is_last:
            vistited[(t_x, t_y)] = True
    
    return ((h_x, h_y), (t_x, t_y))

knots = [(0, 0)] * 10

vistited = {}

for line in f:
    vistited[knots[9]] = True

    # Get movement details
    direction = line[0]
    distance = int(line[2:])

    # Move head
    # The extra adjustment accounts for diagonal movement
    h_x, h_y = knots[0]
    t_x, t_y = knots[1]
    if direction == 'U':
        h_y += distance
    elif direction == 'D':
        h_y -= distance
    elif direction == 'R':
        h_x += distance
    elif direction == 'L':
        h_x -= distance
        
    
    knots[0] = (h_x, h_y)
    knots[1] = (t_x, t_y)

    for i in range(9):
        head = knots[i]
        tail = knots[i + 1]
        knots[i], knots[i + 1] = processMovement(head, tail, i == 8)
    vistited[knots[9]] = True

print(f"Done. Tail visted {str(len(vistited.keys()))} spaces")