# API stuff

from aocd import get_data, submit, lines, numbers
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = data.split("\n\n")
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
answer = len([d for d in data if all(f in d for f in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])])

# submission

submit(answer, part=part, day=day, year=year)
