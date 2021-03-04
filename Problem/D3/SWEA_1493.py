import sys
sys.stdin = open("./Input_Data/D3/1493.txt","r")

for T in range(int(input())):
    p,q = map(int,input().split())
    d = []
    temp = 0
    for i in range(0,1000): # P에 대한 x,y 좌표 d[0],d[1]
        temp+=i
        if p<=temp:
            d.append(i-temp+p)
            d.append(i+1-d[0])
            break
    temp = 0
    for i in range(0,1000): # Q에 대한 x,y 좌표 d[2],d[3]
        temp+=i
        if q<=temp:
            d.append(i-temp+q)
            d.append(i+1-d[2])
            break
    d[0] = d[0] + d[2] # 구하고자 하는 x 좌표
    d[1] = d[1] + d[3] # 구하고자 하는 y 좌표
    p =0
    for i in range(0,d[0]+d[1]-1): p+=i
    print("#{} {}".format(T+1, p+d[0]))