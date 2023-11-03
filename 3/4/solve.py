import re

def check_board(board,seq_num):
    bang = []
    tracker = {"x":[0,0,0,0,0],"y":[0,0,0,0,0],"z1":0,"z2":0}
    for num in seq_num:
        for x, line_x in enumerate(board):
            for y,num_y in enumerate(line_x):
                if num_y == num:
                    tracker["x"][x] += 1
                    tracker["y"][y] += 1
                    bang.append((x,num_y))

                    if(x == y):
                        tracker["z1"] += 1
                    if(x == 4 - y):
                        tracker["z2"] += 1

        for i,x in enumerate(tracker["x"]):
            if ( x == 5):
                # print(i,"bingo")
                # print(board[i])
                return num
        for i,num_y in enumerate(tracker["y"]):
            if ( num_y == 5):
                res = []
                for yy in range(5):
                    res.append(board[yy][i])
                # print(res)
                return num
        if(tracker["z1"] == 5):
            return num
        if(tracker["z2"] == 5) :
            return num
    return False

with open("./input4") as f :
    input = f.read()
    input = input.splitlines()
    seq_num = input[0].split(',')
    # print(seq_num)
    boards = input[2:]
    board_list = []
    for x in range(0,len(boards),6) :
        board_list.append(map(lambda x : re.split('\s+',x.strip()),boards[x:x+5]))
    # print(seq_num)
    for seq in range(len(seq_num)):
        res = False
        current_seq = seq_num[0:seq]

        if(len(board_list) == 1):
            last_b = board_list[0]
            print("lasttt",last_b)
            res = check_board(last_b,current_seq)
            uncheck = []
            for x in last_b:
                for y in x:
                    if y not in current_seq:
                        uncheck.append(y)
            # print("list",uncheck)
            sum = 0
            for uncheck_num in uncheck:
                sum += int(uncheck_num)
            print("sum",sum,res)

            print(sum * int(res))


        for b_i ,b in enumerate(board_list):
            res = check_board(b,current_seq)
            if(res):
                uncheck = []
                # for x in b:
                #     for y in x:
                #         if y not in current_seq:
                #             uncheck.append(y)
                # # print("list",uncheck)
                # sum = 0
                # for uncheck_num in uncheck:
                #     sum += int(uncheck_num)
                board_list.pop(b_i)
#                 print("sum",sum)


# 
#                 
#                 
#                 print(current_seq)
#                 print(int(res) * sum)
        

        # if(res):
        #     break
            

    








#     print(boards)
#     board = []
#     board_list = []
#     for l in boards:
#         if(l == ''):
#             boards.append(board)
#         else:
#             board.append(l)
# 
#         pass

