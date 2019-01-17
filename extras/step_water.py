## 1
def get_perimeter(): pass


def next_k(): pass


## 2
def list_to_int(): pass


def int_to_list(): pass


## 3
def max_wall_pos(data):
    if len(data) <= 1:
        return 0

    pos, val = 0, data[0]
    for n, i in enumerate(data):
        if i > val:
            pos, val = n, i
    return pos


def get_walls_left(data, pos):
    walls = []
    while pos > 0:
        t = max_wall_pos(data[:pos])
        walls.append((t, pos))
        pos = t
    return walls


def get_walls_right(data, pos):
    walls = []
    while pos < len(data) - 1:
        t = max_wall_pos(data[pos + 1:]) + pos + 1
        walls.append((pos, t))
        pos = t
    return walls


def how_many_water(walls, data):
    val = 0
    for l, r in walls:
        if min(l, r) > 0 and r - l > 1:
            val += (r - l - 1) * min(data[l], data[r]) - sum(data[l + 1: r])
            print(l, r, val)
    return val


def calc_water(steps):
    if len(steps) <= 2:
        return 0

    walls = []
    pos = max_wall_pos(steps)
    walls.extend(get_walls_left(steps, pos))
    walls.extend(get_walls_right(steps, pos))
    print(walls)
    print(how_many_water(walls, steps))


calc_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
