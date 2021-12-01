file = open("./preps/2017/2/input.txt", "r")
input = [[int(c) for c in row.split()] for row in file.read().split('\n')]

output = [abs(min(n) - max(n)) for n in input]
sum = sum(output)

print("Sum part 1", sum)

sum = 0
for row in input:
    for i1, n1 in enumerate(row):
        for i2, n2 in enumerate(row):
            if (n1 / n2).is_integer() == True and i1 is not i2:
                sum += n1 / n2

print("Sum part 2", int(sum))