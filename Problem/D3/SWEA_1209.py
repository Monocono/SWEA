import sys
sys.stdin = open("./Input_Data/D3/1209.txt","r")

for T in range(10):
    tc = int(input())
    rl = [list(map(int,input().strip().split())) for _ in range(100)]
    cl = list(map(list,zip(*rl)))
    res = []
    for i in range(100):
        res.append(sum(cl[i]))
        res.append(sum(rl[i]))
    temp_r = temp_c = 0
    for i in range(100):
        temp_r += rl[i][i]
        temp_c += cl[i][i]
    res.append(temp_c)
    res.append(temp_r)
    print('#{} {}'.format(tc, max(res)))