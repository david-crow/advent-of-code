# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)
lines = data.splitlines()

# solution

x, y = 25, 6
layers = [data[i : i + x * y] for i in range(0, len(data), x * y)]
min_layer = min(layers, key=lambda layer: layer.count("0"))
answer = min_layer.count("1") * min_layer.count("2")

# submission

submit(answer, part=part, day=day, year=year)
