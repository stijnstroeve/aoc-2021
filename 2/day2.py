file = open("./2/input.txt", "r")
input = file.read().split("\n")

# Part 1
x = 0
y = 0

for line in input:
    step = line.split(" ")[0]
    amount = int(line.split(" ")[1])

    if step == 'forward':
        x += amount
    elif step == 'down':
        y += amount
    elif step =='up':
        y -= amount

print("Part 1:", x * y)

# Part 2
x = 0
y = 0
a = 0

for line in input:
    step = line.split(" ")[0]
    amount = int(line.split(" ")[1])

    if step == 'forward':
        x += amount
        y += amount * a
    elif step == 'down':
        a += amount
    elif step =='up':
        a -= amount

print("Part 2:", x * y)