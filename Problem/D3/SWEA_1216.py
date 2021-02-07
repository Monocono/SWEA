import sys
sys.stdin = open("./Input_Data/D3/1216.txt","r")

for T in range(10):
    n = 100
    k, res = 1,1
    tc = int(input())
    rl = [list(map(str,input())) for _ in range(n)]
    cl = list(map(list,zip(*rl)))
    flag = False
    for a in range(100):
        flag = False
        for b in range(100):
            for c in range(101-k):
                row = rl[b][c:c+k]
                col = cl[b][c:c+k]
                if row == row[::-1] or col == col[::-1]:
                    res = k
                    flag = True
                    break
            if flag:
                break
        k +=1
    print("#{} {}".format(tc, res))

# 시간이 너무 오래걸림