import datetime

list0 = []
list1 = []


def calc_distance(list0, list1):
    distance = 0

    ptr = 0
    for entry in list0:
        dst = list1[ptr] - list0[ptr]
        if dst < 0:
            dst = -dst

        # print(list0[ptr], " and ", list1[ptr], "distance", dst)
        distance += dst

        ptr += 1

    print("distance", distance)


def calc_similarity(list0, list1):
    similarity = 0

    ptr = 0
    for entry in list0:

        sim = list0[ptr] * list1.count(list0[ptr])
        similarity += sim

        ptr += 1

    print("similarity", similarity)


with open("puzzle1.txt", encoding="utf-8") as file:
    for line in file:
        lists = line.split()
        list0.append(int(lists[0]))
        list1.append(int(lists[1]))

list0.sort()
list1.sort()

a = datetime.datetime.now()
calc_distance(list0, list1)
b = datetime.datetime.now()
print(b - a)

a = datetime.datetime.now()
calc_similarity(list0, list1)
b = datetime.datetime.now()
print(b - a)
