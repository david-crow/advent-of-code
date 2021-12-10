# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

scores = {")" : 3, "]" : 57, "}" : 1197, ">" : 25137}
pairs = {"(" : ")" , "[" : "]" , "{" : "}" , "<" : ">"}
left = list(pairs.keys())
stack = []
answer = 0

for k, v in list(pairs.items()):
    pairs[v] = k

def check(line):
    for char in line:
        if char in left:
            stack.append(char)
        else:
            if pairs[char] != stack.pop(-1):
                return scores[char]

    return 0

for line in data.split("\n"):
    answer += check(line)

# submission

submit(answer, part=part, day=day, year=year)
