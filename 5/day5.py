import collections

file = open('./5/input.txt', 'r')
input = file.read().splitlines()

lines = [[[int(z) for z in y.split(",")] for y in x.split(" -> ")] for x in input]

# Only vertical and horizontal lines
def is_straight_line(line):
    return line[0][0] == line[1][0] or line[0][1] == line[1][1]

def process_lines_part1(lines):
    coords = []

    for line in lines:
        x1 = line[0][0]
        y1 = line[0][1]
        x2 = line[1][0]
        y2 = line[1][1]

        dx = abs(x1 - x2) + 1
        dy = abs(y1 - y2) + 1

        xs = x1 if x1 <= x2 else x2
        ys = y1 if y1 <= y2 else y2

        if dx > 0 and dy == 1:
            for x in range(dx):
                xa = x + xs
                ya = y1
                coords.append((xa, ya))

        if dy > 0 and dx == 1:
            for y in range(dy):
                xa = line[0][0]
                ya = y + ys
                coords.append((xa, ya))
    
    overlap = [item for item, count in collections.Counter(coords).items() if count > 1]
    return len(overlap)


def process_lines_part2(lines):
    coords = []

    for line in lines:
        x1 = line[0][0]
        y1 = line[0][1]
        x2 = line[1][0]
        y2 = line[1][1]

        dx = abs(x1 - x2) + 1
        dy = abs(y1 - y2) + 1

        xs = x1 if x1 <= x2 else x2
        ys = y1 if y1 <= y2 else y2

        if dx > 0 and dy == 1:
            for x in range(dx):
                xa = x + xs
                ya = y1
                coords.append((xa, ya))

        if dy > 0 and dx == 1:
            for y in range(dy):
                xa = line[0][0]
                ya = y + ys
                coords.append((xa, ya))
        elif dx == dy:
            y = 0
            for x in range(dx):
                ux = x1 - x2 < 0
                uy = y1 - y2 < 0
                
                xa = x1 + x if ux else x1 - x
                ya = y1 + y if uy else y1 - y

                coords.append((xa, ya))
                y += 1
    
    overlap = [item for item, count in collections.Counter(coords).items() if count > 1]
    return len(overlap)


lines_part1 = list(filter(is_straight_line, lines))
print("Part1:", process_lines_part1(lines_part1))
print("Part2:", process_lines_part2(lines))