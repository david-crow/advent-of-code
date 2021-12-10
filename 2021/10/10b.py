# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

scores = {")" : 1, "]" : 2, "}" : 3, ">" : 4}
pairs = {"(" : ")" , "[" : "]" , "{" : "}" , "<" : ">"}
left = list(pairs.keys())
incomplete_scores = []
stack = []

for k, v in list(pairs.items()):
    pairs[v] = k

def check(line):
    stack = []

    for char in line:
        if char in left:
            stack.append(char)
        else:
            if pairs[char] != stack.pop(-1):
                return None

    return stack

for line in data.split("\n"):
    stack = check(line)

    if stack != None:
        closing = list(reversed("".join(stack)))
        score = 0

        for char in closing:
            score *= 5
            score += scores[pairs[char]]

        incomplete_scores.append(score)

incomplete_scores.sort()
answer = incomplete_scores[len(incomplete_scores) // 2]

# submission

submit(answer, part=part, day=day, year=year)
