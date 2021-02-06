import sys
sys.stdin = open("./Input_Data/D3/1220.txt","r")

for T in range(10):
    n = int(input())
    table = [list(map(int,input().strip().split())) for _ in range(n)]
    res = 0
    for i in range(n):
        flag = False
        for j in range(n):
            if table[j][i] == 1:
                flag = True
            if table[j][i] == 2 and flag == True:
                flag = False
                res+=1
    print("#{} {}".format(T+1,res))