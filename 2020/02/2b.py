# API stuff

from aocd import get_data, submit, lines, numbers
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = [d.split(" ") for d in lines]
data = [(list(map(int, d[0].split("-"))), d[1][0], d[2]) for d in data]
answer = len([password for idx, c, password in data if (c == password[idx[0] - 1]) != (c == password[idx[1] - 1])])

# submission

submit(answer, part=part, day=day, year=year)
