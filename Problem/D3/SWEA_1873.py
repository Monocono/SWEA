import sys
sys.stdin = open("./Input_Data/D3/1873.txt","r")

move_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
command_dict = {'U' : 0, 'D' : 1, 'L' : 2, 'R' : 3, 'S' :4,
'^' : 0, 'v' : 1, '<': 2, '>': 3, 0: '^', 1: 'v', 2:'<', 3:'>'}
serch_list = ['<', '>', '^', 'v']

for T in range(int(input())):
    H, W = map(int, input().split())
    map_list = [list(input()) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if map_list[i][j] in serch_list:
                tank_pos = (i, j, command_dict[map_list[i][j]])
                break
        else: continue
        break
    input()
    commands = input()
    for command in commands:
        temp = command_dict[command]
        if temp == 4:
            dy = tank_pos[0] 
            dx = tank_pos[1]
            while True:
                dy += move_list[tank_pos[2]][0]
                dx +=move_list[tank_pos[2]][1]
                if 0 > dy or dy >= H or 0 > dx or dx >= W or map_list[dy][dx] == '#':
                    break
                if map_list[dy][dx] == '*':
                    map_list[dy][dx] = '.'
                    break
        else:
            y = tank_pos[0]
            x = tank_pos[1]
            dy = y + move_list[temp][0]
            dx = x + move_list[temp][1]
            map_list[y][x] = command_dict[temp]
            tank_pos = (y, x, temp)
            if 0 <= dy < H and 0 <= dx < W and map_list[dy][dx] == '.':
                map_list[y][x] = '.'
                map_list[dy][dx] = command_dict[temp]
                tank_pos = (dy, dx, temp)
    print('#{}'.format(T+1), end=' ')
    for m in map_list:
        print(''.join(m))