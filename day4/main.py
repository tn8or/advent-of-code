maparr = {}
count = 0

with open("puzzle.txt", encoding="utf-8") as file:
    x = 0
    for line in file:
        maparr[x] = {}
        y = 0
        for ch in line:
            if ch != "\n":
                maparr[x][y] = ch
                y += 1
        x += 1


def find_the_x(maparr):
    y = 0
    for row in maparr.values():
        x = 0
        for col in row.values():
            if col == "X":
                print("found one at x", x, " y", y)
                check_perimeter(maparr, x, y)
            x += 1
        y += 1


def check_perimeter(maparr, x, y):
    ## combinations of xmas:
    #      -1,0   1,0
    #      SAMX   XMAS
    #  0,-1 -1,-1  1,-1
    #  S    S        S
    #  A     A      A
    #  M      M    M
    #  X       X  X
    #  0,1  -1,1  1,1
    #  X       X  X
    #  M      M    M
    #  A     A      A
    #  S    S        S

    # find max size of the map
    xmax = len(maparr)
    ymax = len(maparr[0])

    # based on available space, which should we search for?

    # XMAS variants
    if (x + 3) <= len(maparr[0]) - 1:
        # level
        find_string(
            maparr=maparr, string="XMAS", x=x, y=y, xprogression=1, yprogression=0
        )
        # diagonal down
        if (y + 3) <= len(maparr) - 1:
            find_string(
                maparr=maparr, string="XMAS", x=x, y=y, xprogression=1, yprogression=1
            )
        # diagonal up
        if (y - 3) >= 0:
            find_string(
                maparr=maparr, string="XMAS", x=x, y=y, xprogression=1, yprogression=-1
            )
    # SAMX variants
    if (x - 3) >= 0:
        # level
        find_string(
            maparr=maparr, string="XMAS", x=x, y=y, xprogression=-1, yprogression=0
        )
        # diagonal down
        if (y + 3) <= len(maparr) - 1:
            find_string(
                maparr=maparr, string="XMAS", x=x, y=y, xprogression=-1, yprogression=1
            )
        # diagonal up
        if (y - 3) >= 0:
            find_string(
                maparr=maparr, string="XMAS", x=x, y=y, xprogression=-1, yprogression=-1
            )
    # vertical down
    if (y + 3) <= len(maparr) - 1:
        find_string(
            maparr=maparr, string="XMAS", x=x, y=y, xprogression=0, yprogression=1
        )
        # vertical up
    if (y - 3) >= 0:
        find_string(
            maparr=maparr, string="XMAS", x=x, y=y, xprogression=0, yprogression=-1
        )


def find_string(maparr, string, x, y, xprogression, yprogression):
    global count
    ptr = 0
    for char in string:
        xlocation = x + (ptr * xprogression)
        ylocation = y + (ptr * yprogression)
        # print("SEARCY CHAR ", char, " at y ", ylocation, "x ", xlocation)
        if maparr[ylocation][xlocation] == char:
            #            print("FOUND CHAR ", char, " at y ", ylocation, "x ", xlocation)
            if char == "S":
                count += 1
        else:
            return False
        ptr += 1


find_the_x(maparr)

print("total: ", count)
