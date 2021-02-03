import sys
sys.stdin = open("./Input_Data/D2/1288.txt","r")

for T in range(int(input())):
    n = int(input())
    cnt = 0
    s=[str(_) for _ in range(10)]
    while s:
        cnt +=1
        nk= n*cnt
        nk=str(nk)
        for c in nk:
            if c in s:
                s.remove(c)
    print("#{} {}".format(T+1, n*cnt))
