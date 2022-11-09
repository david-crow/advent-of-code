# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = [d.split() for d in data.split("\n")]
lcd = [[0 for _ in range(50)] for _ in range(6)]

for ins in data:
    if ins[0] == "rect":
        vals = list(map(int, ins[1].split("x")))

        for row in range(vals[1]):
            for col in range(vals[0]):
                lcd[row][col] = 1

    else:
        vals = [int(ins[2].split("=")[1]), int(ins[4])]

        # rotate column
        if ins[1] == "column":
            col = [row[vals[0]] for row in lcd]
            col = col[-vals[1]:] + col[:-vals[1]]

            for i in range(len(lcd)):
                lcd[i][vals[0]] = col[i]

        # rotate row
        else:
            row = lcd[vals[0]]
            row = row[-vals[1]:] + row[:-vals[1]]
            lcd[vals[0]] = row

lcd = ["".join(list(map(str, row))).replace("0", " ").replace("1", "#") for row in lcd]

for row in lcd:
    print("".join(map(str, row)))

# submission

answer = "AFBUPZBJPS"
submit(answer, part=part, day=day, year=year)
