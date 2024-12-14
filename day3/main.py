sum = 0
file_path = "puzzle.txt"


with open(file_path, "r") as file:
    file_content = file.read()


do = file_content.split("do()")

for dos in do:
    dont = dos.split("don't()")
    split = dont[0].split("mul(")
    print(split)

    for occurrence in split:
        content = occurrence.split(")")
        numbers = content[0].split(",")
        if numbers[0].isdigit() and numbers[1].isdigit():
            result = int(numbers[0]) * int(numbers[1])
            sum += result
            # print(result)


print("final result", sum)
