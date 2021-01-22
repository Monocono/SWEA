import sys
sys.stdin=open("./Input_Data/D1/2056.txt","r")

D = [31,28,31,30,31,30,31,31,30,31,30,31]
for T in range(int(input())):
    s=input()
    m=int(s[4:6])
    d=int(s[6:8])
    res=-1
    if 1<=m and m <=12 and 1<=d and d<=D[m-1]:
        res=s[0:4]+"/"+s[4:6]+"/"+s[6:8]
    print("#{} {}".format(T+1, res))

