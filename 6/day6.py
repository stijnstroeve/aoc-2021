file = open('./6/input.txt', 'r')
input = [int(x) for x in file.read().split(',')]

fish_ages = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0
}

def initialize_ages(input, fish_ages):
    # Reset ages
    for age in fish_ages:
        fish_ages[age] = 0

    # Parse input ages
    for n in input:
        fish_ages[n] += 1

def do_generation(fish_ages):
    # I know this is hardcoded with way too many array-accesses, but it works go enough so who cares :P
    tmp = fish_ages[1]

    fish_ages[1] = fish_ages[2]
    fish_ages[2] = fish_ages[3]
    fish_ages[3] = fish_ages[4]
    fish_ages[4] = fish_ages[5]
    fish_ages[5] = fish_ages[6]
    fish_ages[6] = fish_ages[7] + fish_ages[0]
    fish_ages[7] = fish_ages[8]

    fish_ages[8] = fish_ages[0]
    fish_ages[0] = tmp

def do_generations(input, fish_ages, generations):
    initialize_ages(input, fish_ages)

    for i in range(generations):
        do_generation(fish_ages)

    return sum(fish_ages.values())

print("Part1:", do_generations(input, fish_ages, 80))
print("Part2:", do_generations(input, fish_ages, 256))