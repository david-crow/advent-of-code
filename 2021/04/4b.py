# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

def isBingo(mask):
    for i in range(0, 25, 5):
        if all(mask[i : i + 5]):
            return True

    for i in range(5):
        column = []

        for j in range(i, 25, 5):
            column.append(mask[j])

        if all(column):
            return True
    
    return False

def boardSum(board, mask):
    return sum(0 if mask[i] else board[i] for i in range(25))

def main():
    nums = [int(n) for n in data.split("\n")[0].split(",")]
    lines = [line.strip() for line in data.split("\n")[1:]]
    boards = []

    for i in range(1, len(lines), 6):
        boards.append([int(n) for n in " ".join(lines[i : i + 5]).split()])

    masks = [[False] * 25 for _ in range(len(boards))]
    solved_boards = [False] * len(boards)

    for num in nums:
        for i, board in enumerate(boards):
            if num in board:
                masks[i][board.index(num)] = True

                if isBingo(masks[i]):
                    solved_boards[i] = True

                    if all(solved_boards):
                        return num * boardSum(board, masks[i])

answer = main()

# submission

submit(answer, part=part, day=day, year=year)
