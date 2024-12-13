import datetime

reports = []
safereports = 0

with open("reports.txt", encoding="utf-8") as file:
    for line in file:
        reports.append(list(map(int, line.split())))


def is_safe_report(report):
    direction = 0
    ptr = 0
    for level in report:

        if ptr < len(report) - 1:
            current = level
            next = report[ptr + 1]
            diff = next - current

            if direction == 0:
                if diff > 0:
                    direction = "+"
                    print("direction: ", direction)
                elif diff < 0:
                    direction = "-"
                    print("direction: ", direction)
                else:
                    print("wrong direction")
                    return False

            if direction == "+":
                if diff < 0 or diff < 1 or diff > 3:
                    print(current, next, diff, "out of bounds")
                    return False
                else:
                    print(current, next, diff, " in bounds")

            elif direction == "-":
                if -diff < 0 or -diff < 1 or -diff > 3:
                    print(current, next, diff, "out of bounds")
                    return False
                else:
                    print(current, next, diff, " in bounds")
            else:
                print("I have direction ... towards the mall")
                return False
        ptr += 1
    return True


def remove_one_record(report):
    for i in range(len(report)):
        tempreport = report.copy()
        tempreport.pop(i)
        print("trying: ", tempreport)

        if is_safe_report(tempreport):
            return True
    return False


a = datetime.datetime.now()

for report in reports:
    print(report)
    if is_safe_report(report):
        print("safe!")
        safereports += 1
    else:
        if remove_one_record(report):
            print("now safe!")
            safereports += 1
        else:
            print("not safe!")

print("safe reports: ", safereports)
b = datetime.datetime.now()
print(b - a)
