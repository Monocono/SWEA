import sys
sys.stdin= open("./Input_Data/D3/1206.txt","r")

init=[0,0]
for T in range(10):
    w=int(input())
    ws=list(map(int,input().split()))
    res=0
    ws.extend(init); ws.reverse(); ws.extend(init) 
    for i in range(2,len(ws)-2):
        m=max(max(ws[i-1],ws[i-2]),max(ws[i+1],ws[i+2]))
        if m<ws[i]: 
            res+=ws[i]-m 
    print("#{} {}".format(T+1, res))