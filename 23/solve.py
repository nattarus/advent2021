from operator import itemgetter
import copy


class Diagram:
    def __init__(self, di):
        self.di = di

    def print(self):
        max_x = max(self.di.keys(), key=itemgetter(0))[0] + 1
        max_y = max(self.di.keys(), key=itemgetter(1))[1] + 1
        temp = [list(" " for _ in range(max_y)) for _ in range(max_x)]
        for k, v in self.di.items():
            temp[k[0]][k[1]] = v
        # print("".join(map(str, range(max_y))))
        for line in temp:
            print("".join(map(str, line)))

    def __eq__(self, other):
        if not isinstance(other, Diagram):
            return False
        for k in self.di:
            if self.di[k] != other.di[k]:
                return False
            # if self.di[(0, 1)] != other.di[0, 1]:
            # return False
        return True

    def move_h(self, fr, to):
        assert fr[0] == 1
        assert to[0] == 1
        if fr[1] == to[1]:
            print(fr, to)
            self.print()

        if fr[1] < to[1]:
            for i in range(fr[1] + 1, to[1] + 1):
                if self.di[(1, i)] != ".":
                    return False

        if fr[1] > to[1]:
            for i in range(to[1], fr[1]):
                if self.di[(1, i)] != ".":
                    return False

        return True

    # def move_v(self, fr, to):
    #     if fr[1] not in [3, 5, 7, 9]:
    #         return False
    #
    #     if fr[0] < to[0]:
    #         for i in range(fr[0], to[0] + 1):
    #             if self.di[i, fr[1]] != ".":
    #                 return False
    #     if fr[0] > to[0]:
    #         for i in range(to[0], fr[0] + 1):
    #             if self.di[i, fr[1]] != ".":
    #                 return False
    #
    #     # if fr[0] == to[0]:
    #     #     return False
    #
    #     return True

    def can_move_out(self, fr, to):
        for i in range(to[0], fr[0]):
            if self.di[i, fr[1]] != ".":
                return False
        return True

    def can_move_hori(self, pos):
        temp = []
        halls = self.get_empty_hall()

        for h in halls:
            if self.move_h((1, pos[1]), h):
                temp.append(h)
        if len(temp) == 0:
            # print("Error")
            return False
        return temp

    def get_empty_hall(self):
        temp = []
        for k, v in self.di.items():
            if v == "." and k[0] == 1 and k[1] not in [3, 5, 7, 9]:
                temp.append(k)
        return temp

    def get_ambi(self):
        temp = []
        for k, v in self.di.items():
            if isinstance(v, Ambi):
                temp.append((k, v))
        return temp

    def get_room(self, room_no):
        for i in range(2, 6)[::-1]:
            spot = self.di[(i, room_no)]
            if spot == ".":
                return (i, room_no)
            if isinstance(spot, Ambi) and spot.des != room_no:
                return False

    def sum_energy(self):
        ambis = self.get_ambi()
        sum = 0
        for i in ambis:
            sum += i.energy
        return sum

    def check_room(self, room_no):
        for i in range(2, 6)[::-1]:
            spot = self.di[(i, room_no)]
            if spot == ".":
                return False
            if isinstance(spot, Ambi) and spot.des != room_no:
                return False
        return True

    def check_rooms(self):
        a = self.check_room(3)
        b = self.check_room(5)
        c = self.check_room(7)
        d = self.check_room(9)
        if a and b and c and d:
            return True
        return False

    def move_ambi(self, fr, to):
        temp = self.di[fr]
        self.di[fr] = "."
        temp.walk(fr, to)
        temp.in_room = False
        self.di[to] = temp

    def move_in(self, fr, to):
        temp = self.di[fr]
        self.di[fr] = "."
        temp.walk(fr, to)
        temp.is_complete = True
        temp.in_room = True
        self.di[to] = temp

    def turn(self):
        temp = []
        ambis = self.get_ambi()
        if self.check_rooms():
            print(self.sum_energy())
        for pos, a in ambis:
            if not a.in_room and not a.is_complete:
                room = self.get_room(a.des)
                if room:
                    can_move_in = self.move_h((1, pos[1]), (1, a.des))
                    if can_move_in:
                        copy_di = copy.deepcopy(self.di)
                        diag = Diagram(copy_di)
                        diag.move_in(pos, room)
                        temp.append(diag)

            if a.in_room and self.can_move_out(pos, (1, pos[1])):
                # print(a)
                halls = self.can_move_hori(pos)
                if halls:
                    for h in halls:
                        copy_di = copy.deepcopy(self.di)
                        diag = Diagram(copy_di)
                        diag.move_ambi(pos, h)
                        temp.append(diag)
                        # compare = False
                        # for i in temp:
                        #     if diag == i:
                        #         compare = True
                        # if not compare:
                        #     temp.append(diag)
                        # else:
                        #     ma = list(filter(lambda x: x == diag, temp))
                        #     for i in ma:
                        #         if i.sum_energy() > diag.sum_energy():
                        #             temp.remove(i)
                        #             temp.append(diag)

        return temp


ambi_room = {"A": 3, "B": 5, "C": 7, "D": 9}
ambi_val = {"A": 1, "B": 10, "C": 100, "D": 1000}


class Ambi:
    def __init__(self, pos, type):
        self.type = type
        self.des = ambi_room[type]
        self.is_complete = False
        self.in_room = True
        if pos[0] == 1:
            self.in_room = False
        self.energy = 0

    def __eq__(self, other):
        if not isinstance(other, Ambi):
            return False
        return self.type == other.type

    def walk(self, fr, to):
        diff_x = abs(fr[0] - to[0])
        diff_y = abs(fr[1] - to[1])
        sum = diff_y + diff_x
        self.energy += sum * ambi_val[self.type]

    def __str__(self):
        return f"{self.type}"


def read_parse():
    with open("./input") as f:
        f = f.read()
        di = {}
        for i, line in enumerate(f.splitlines()):
            for j, dot in enumerate(list(line)):
                # if dot == "#":
                #     di[(i, j)] = "#"
                if dot in ["A", "B", "C", "D"]:
                    di[(i, j)] = Ambi((i, j), dot)
                if dot == ".":
                    di[i, j] = "."
        di = Diagram(di=di)
        return di


def turn_digram(di: list[Diagram]):
    temp = []
    for d in di:
        # d.print()
        possible = d.turn()
        # print_m(possible)
        for p in possible:
            temp.append(p)
    return temp


def print_m(m: list[Diagram]):
    for i in m:
        i.print()


def main():
    di = read_parse()
    result = turn_digram([di])
    # result = turn_digram(result)
    # result = turn_digram(result)
    # print_m(result)

    while len(result) > 0:
        result = turn_digram(result)
        print(len(result))


main()
