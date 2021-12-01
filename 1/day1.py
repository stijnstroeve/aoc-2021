file = open("./1/input.txt", "r")
input =  file.read().split("\n")

# Part 1
prev = 0
higher = 0

for i, measurement in enumerate(input):
    measurement = int(measurement)

    if measurement > prev and i != 0:
        higher += 1

    prev = measurement

print("Part 1 sum:", higher)

# Part 2
prev = 0
higher = 0

for i, measurement in enumerate(input):
    if i + 1 >= len(input) or i + 2 >= len(input): continue

    sum = int(input[i]) + int(input[i + 1]) + int(input[i + 2])

    if sum > prev and i != 0:
        higher += 1

    prev = sum

print("Part 2 sum:", higher)
