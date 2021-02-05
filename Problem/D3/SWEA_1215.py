import sys
sys.stdin = open("./Input_Data/D3/1215.txt","r")

for T in range(10):
    k = int(input())
    rl =[list(map(str,input())) for _ in range(8)]
    cl = list(map(list,zip(*rl)))
    res = 0
    for i in range(8):
        for j in range(9-k):
            row=rl[i][j:j+k]
            col=cl[i][j:j+k]
            if row == row[::-1]: res+=1
            if col == col[::-1]: res+=1
    print("#{} {}".format(T+1,res))