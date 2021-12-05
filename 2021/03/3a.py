# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
year, day = int(__file__.split("/")[-3]), int(__file__.split("/")[-2])
data = get_data(day=day, year=year)

# solution

import numpy as np

data = np.array([list(map(int, list(d))) for d in data.split()])
sums = np.sum(data, axis=0)
gamma = (sums > np.shape(data)[0] / 2).astype(int)
epsilon = (gamma == 0).astype(int)
answer = int("".join(gamma.astype(str)), 2) * int("".join(epsilon.astype(str)), 2)

# submission

submit(answer, part=part, day=day, year=year)
