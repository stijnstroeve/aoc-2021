class BoardCell:
    def __init__(self, number=0, is_marked=False):
        self.number = number
        self.is_marked = is_marked

file = open('./4/input.txt', 'r')
input = file.read()

numbers = [int(x) for x in input.splitlines()[0].split(',')]

raw_boards = input.split("\n\n")
raw_boards.pop(0)

boards = []
for raw_board in raw_boards:
    board = [[BoardCell(int(y), False) for y in x.split(' ') if y.strip() != ''] for x in raw_board.splitlines()]
    boards.append(board)

def reset_boards(boards):
    for board in boards:
        for y in board:
            for cell in y: 
                cell.is_marked = False

def unmarked_numbers_sum(board):
    sum = 0
    for y in board:
        for cell in y:            
            if cell.is_marked is False:
                sum += cell.number

    return sum

def check_board_win(board):
    win = False
    
    for y in board:
        all_marked = True

        for cell in y:
            if cell.is_marked is False:
                all_marked = False
        
        if all_marked:
            win = True

    for x, xV in enumerate(board[0]):
        all_marked = True
        
        for y in range(len(board)):
            cell = board[y][x]
            if cell.is_marked is False:
                all_marked = False

        if all_marked:
            win = True

    return win

def mark_number(boards, number):
    for board in boards:
        for y in board:
            for cell in y:            
                if cell.number == number:
                    cell.is_marked = True

def check_numbers_part1(boards, numbers):
    for number in numbers:
        mark_number(boards, number)

        for board in boards:
            win = check_board_win(board)

            if win:
                return unmarked_numbers_sum(board) * number

    return -1

def check_numbers_part2(boards, numbers):
    wins = []
    has_won = []

    for number in numbers:
        mark_number(boards, number)

        for board in boards:
            if board not in has_won:
                win = check_board_win(board)

                if win:
                    wins.append(unmarked_numbers_sum(board) * number)
                    has_won.append(board)

    return wins[len(wins) - 1]

print("Part1:", check_numbers_part1(boards, numbers))
reset_boards(boards)
print("Part2:", check_numbers_part2(boards, numbers))