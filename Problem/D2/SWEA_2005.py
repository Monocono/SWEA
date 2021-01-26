import sys
sys.stdin=open("./Input_Data/D2/2005.txt","r")

for T in range(int(input())):
    dep= int(input())
    res=[]
    for i in range(0,dep):
        row=[]
        for j in range(i+1):
            if j ==0 or j==i:
                row.append(1)
            else:
                row.append(res[i-1][j-1]+res[i-1][j])
        res.append(row)
    print("#{}".format(T+1))
    for _ in res:
        print(' '.join(map(str,_)))