# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = [[d.split()[:10], d.split()[-4:]] for d in data.split("\n")]
uniques = {2: 1, 4: 4, 3: 7, 7: 8}
answer = 0

for line in data:
    inp = [set(word) for word in line[0]]
    out = [set(word) for word in line[1]]

    nums = [-1] * 10

    # 1, 4, 7, 8
    for word in inp:
        if len(word) in uniques.keys():
            nums[uniques[len(word)]] = word

    for i in [1, 4, 7, 8]:
        inp.remove(nums[i])

    # the rest
    for word in inp:
        if nums[4].issubset(word): 
            nums[9] = word
        elif len(word) == 6 and not nums[4].issubset(word):
            if nums[7].issubset(word):
                nums[0] = word
            else:
                nums[6] = word
        elif len(word) == 5:
            if nums[1].issubset(word):
                nums[3] = word
            elif len(word.intersection(nums[4])) == 2:
                nums[2] = word
            else:
                nums[5] = word

    answer += int("".join([str(nums.index(word)) for word in out]))

# submission

submit(answer, part=part, day=day, year=year)
