# --- Part Two ---

    # On the other hand, it might be wise to try a different strategy: let the giant squid win.

    # You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

    # In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

    # Figure out which board will win last. Once it wins, what would its final score be?

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
    with open("Problem 4/4-1.dat", "r") as f:
        nums = [int(n) for n in f.readline().split(",")]
        lines = [line.strip() for line in f.readlines()]

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

if __name__ == "__main__":
    print(main())
