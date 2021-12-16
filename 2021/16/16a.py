# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

hexbin = {
    "0":"0000",
    "1":"0001",
    "2":"0010",
    "3":"0011",
    "4":"0100",
    "5":"0101",
    "6":"0110",
    "7":"0111",
    "8":"1000",
    "9":"1001",
    "A":"1010",
    "B":"1011",
    "C":"1100",
    "D":"1101",
    "E":"1110",
    "F":"1111"
}

data = "".join(hexbin[d] for d in data.strip("0"))
answer = 0

def parse(data):
    global answer
    version = int(data[:3], 2)
    data = data[3:]
    answer += version

    tid = int(data[:3], 2)
    data = data[3:]

    if tid == 4:
        val = ""

        while True:
            val += data[1:5]
            flag = data[0]
            data = data[5:]

            if flag == "0":
                break

    else:
        lid = data[0]
        data = data[1:]

        if lid == "0":
            count = int(data[:15], 2)
            data = data[15:]
            subp = data[:count]

            while subp:
                subp = parse(subp)

            data = data[count:]

        else:
            count = int(data[:11], 2)
            data = data[11:]

            for _ in range(count):
                data = parse(data)

    return data

parse(data)

# submission

submit(answer, part=part, day=day, year=year)
