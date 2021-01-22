import sys
sys.stdin= open("./Input_Data/1206.txt","r")

for T in range(10):
    w=int(input())
    #print(w)
    ws=list(map(int,input().split()))
    print(ws)
    res=0
    for i in range(2,len(ws)-2):
        m=max(max(ws[i-1],ws[i-2]),max(ws[i+1],ws[i+2]))
        if m<ws[i]:
            res+=ws[i]-m 
    print("#{} {}".format(T+1, res))