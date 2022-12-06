# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = list(map(int, data.split(",")))

def findPairs(d):
    for a in range(100):
        for b in range(100):
            new_data = d[::]
            new_data[1] = a
            new_data[2] = b

            try:
                for i in range(0, len(new_data), 4):
                    match new_data[i]:
                        case 1:
                            new_data[new_data[i + 3]] = new_data[new_data[i + 1]] + new_data[new_data[i + 2]]
                        case 2:
                            new_data[new_data[i + 3]] = new_data[new_data[i + 1]] * new_data[new_data[i + 2]]
                        case 99:
                            break

            except IndexError:
                pass

            if new_data[0] == 19690720:
                return 100 * a + b

answer = findPairs(data)

# submission

submit(answer, part=part, day=day, year=year)
