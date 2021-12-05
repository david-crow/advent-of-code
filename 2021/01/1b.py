# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
year, day = int(__file__.split("/")[-3]), int(__file__.split("/")[-2])
data = get_data(day=day, year=year)

# solution

data = [int(d) for d in data.split()]
count, previous = 0, sum(data[:3])

for i in range(len(data[1 : -2])):
    newest = sum(data[i + 1 : i + 4])
    count += 1 if newest > previous else 0
    previous = newest

answer = count

# submission

submit(answer, part=part, day=day, year=year)
