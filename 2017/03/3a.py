# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = int(data)
# data = 23
diameter = 1

# figure out how wide the spiral is at the end
while diameter ** 2 < data:
    diameter += 2

# excluding the final layer, we already know how many pieces we've placed
position = (diameter - 2) ** 2

# identify which side the requested data lives on
while position < data:
    position += diameter - 1

# answer = (distance to the center of the side edge) + (distance from the edge to the center)
answer = (diameter // 2 - abs(data - position)) + diameter // 2

# submission

submit(answer, part=part, day=day, year=year)
