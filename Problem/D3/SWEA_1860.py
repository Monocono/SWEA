import sys
sys.stdin = open("./Input_Data/D3/1860.txt","r")

for T in range(int(input())):
    n,m,k=map(int,input().split())
    person = list(map(int,input().split()))
    person.sort()
    flag = True
    for i in range(n):
        p = (person[i]//m)*k # 온시간에 만들수 있는 갯수
        if p < i+1:
            flag = False
            break
    print("#{} {}".format(T+1, "Possible" if flag else "Impossible"))