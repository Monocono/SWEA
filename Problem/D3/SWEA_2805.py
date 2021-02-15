import sys
sys.stdin = open("./Input_Data/D3/2805.txt","r")

for T in range(int(input())):
    n = int(input())
    l = [list(map(int, list(input()))) for _ in range(n)]
    temp = n//2
    change = -1
    res = 0
    for i in range(n):
        if i >= n//2:
            change = 1
        for j in range(abs(i-n//2), abs(n-temp)):
            res += l[i][j]
        temp += change
    print('#{} {}'.format(T+1, res))