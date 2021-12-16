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
        num = ""

        while True:
            num += data[1:5]
            flag = data[0]
            data = data[5:]

            if flag == "0":
                break

        return (data, int(num, 2))

    else:
        lid = data[0]
        data = data[1:]
        values = []

        if lid == "0":
            count = int(data[:15], 2)
            data = data[15:]
            subp = data[:count]

            while subp:
                subp, num = parse(subp)
                values.append(num)

            data = data[count:]

        else:
            count = int(data[:11], 2)
            data = data[11:]

            for _ in range(count):
                data, num = parse(data)
                values.append(num)

        if tid == 0:
            return (data, sum(values))

        if tid == 1:
            prod = 1

            for v in values:
                prod *= v

            return (data, prod)

        if tid == 2:
            return (data, min(values))

        if tid == 3:
            return (data, max(values))

        if tid == 5:
            return (data, 1 if values[0] > values[1] else 0)

        if tid == 6:
            return (data, 1 if values[0] < values[1] else 0)

        if tid == 7:
            return (data, 1 if values[0] == values[1] else 0)

    return data

answer = parse(data)[1]

# submission

submit(answer, part=part, day=day, year=year)
