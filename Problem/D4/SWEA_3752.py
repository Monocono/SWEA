import sys
sys.stdin = open("./Input_Data/D4/3752.txt","r")

for T in range(int(input())):
    n = int(input())
    l = list(map(int,input().strip().split()))
    res = [0]

    for num in l:
        res = list(set(res))
        for i in range(len(res)):
            res.append(res[i]+num)

    print("#{} {}".format(T+1, len(set(res))))