import math

file = open('./7/input.txt', 'r')
input = [int(x) for x in file.read().split(',')]

def part1():
    min_fuel = math.inf
    for target_x in range(1, max(input)):
        sum = 0
        for current_x in input:
            sum += abs(target_x - current_x)

        if sum < min_fuel:
            min_fuel = sum

    return min_fuel
    
def part2():
    min_fuel = math.inf
    for target_x in range(1, max(input)):
        sum = 0
        for current_x in input:
            delta = abs(target_x - current_x)
            triangle_number = (delta * (delta + 1)) // 2
            sum += triangle_number

        if sum < min_fuel:
            min_fuel = sum

    return min_fuel

print("Part1:", part1())
print("Part2:", part2())