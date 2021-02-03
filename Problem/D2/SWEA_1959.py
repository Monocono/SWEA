import sys
sys.stdin = open("./Input_Data/D2/1959.txt","r")

for T in range(int(input())):
    a,b = map(int,input().split(" "))
    a_s = list(map(int,input().split()))
    b_s = list(map(int,input().split()))
    res=[]
    if b>a:
        for pv in range(0,b-a+1):
            temp = 0
            for idx in range(a):
                temp+=a_s[idx]*b_s[pv+idx]
            res.append(temp)
    else:
        for pv in range(0,a-b+1):
            temp = 0
            for idx in range(b):
                temp+=a_s[pv+idx]*b_s[idx]
            res.append(temp)
    print("#{} {}".format(T+1, max(res)))