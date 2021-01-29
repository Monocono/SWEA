import sys
sys.stdin = open("./Input_Data/D2/2001.txt","r")

for T in range(int(input())):
    n, m = map(int,input().split())
    pix= []
    for i in range(n):
        row = list(map(int,input().split()))
        pix.append(row)
    res = 0 
    temp = 0

    for a in range(n-m+1):
        for b in range(n-m+1):
            for c in range(m):
                for d in range(m):
                    temp+=pix[a+c][b+d]
            if res < temp:
                res=temp
            temp = 0
    print("#{} {}".format(T+1, res))
