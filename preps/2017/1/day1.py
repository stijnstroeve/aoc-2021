file = open("./preps/2017/1/input.txt", "r")
input = file.read()

sum = 0
for i, char in enumerate(input):
    ni = 0 if i >= len(input) - 1 else i + 1
    nchar = input[ni]

    if nchar == char:
        sum += int(char)

print("Sum part 1", sum)

sum = 0
hl = round(len(input) / 2)
for i, char in enumerate(input):
    ni = i + hl

    if ni >= len(input) - 1:
        ni -= len(input)

    nchar = input[ni]

    if nchar == char:
        sum += int(char)

print("Sum part 2", sum)
