# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
year, day = int(__file__.split("/")[-3]), int(__file__.split("/")[-2])
data = get_data(day=day, year=year)

# solution

import numpy as np
import copy

o2_data = np.array([list(map(int, list(d))) for d in data.split()])
co2_data = copy.deepcopy(o2_data)
o2_idx, co2_idx = 0, 0

while np.shape(o2_data)[0] > 1:
    val = (o2_data[:, o2_idx].sum() >= np.shape(o2_data)[0] / 2).astype(int)
    o2_data = o2_data[o2_data[:, o2_idx] == val]
    o2_idx += 1

while np.shape(co2_data)[0] > 1:
    val = (co2_data[:, co2_idx].sum() < np.shape(co2_data)[0] / 2).astype(int)
    co2_data = co2_data[co2_data[:, co2_idx] == val]
    co2_idx += 1

o2 = int("".join(o2_data[0].astype(str)), 2)
co2 = int("".join(co2_data[0].astype(str)), 2)

answer = o2 * co2

# submission

submit(answer, part=part, day=day, year=year)
