# x_1 = 20
# x_2 = 30
# y_1 = -10
# y_2 = -5

x_1 = 34
x_2 = 67
y_1 = -215
y_2 = -186


def main(x_v, y_v):
    x_pos = 0
    y_pos = 0
    max_y = 0

    # for i in range(time):
    while y_pos > y_2 or x_pos < x_1:
        if y_v == 0:
            max_y = y_pos

            # print("max_y", r)
        y_pos += y_v
        y_v -= 1
        x_pos += x_v
        if x_v is not 0:
            x_v -= 1
        # print(y_v)
        if y_pos in range(y_1, y_2 + 1) and x_pos in range(x_1, x_2 + 1):
            print("IN", y_pos, x_pos, max_y)
            return 1
        if y_pos < y_1:
            # print("Fail", r)
            return 0
        if x_pos > x_2:
            return 0


sum = 0
for i in range(100):
    # print("i:", i)
    for j in range(-1000, 1000):
        sum += main(i, j)
print(sum)
