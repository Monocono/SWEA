import sys
sys.stdin = open("./Input_Data/D3/6958.txt","r")

for T in range(int(input())):
    n ,m = map(int,input().split())
    l =[list(map(int,input().strip().split())) for _ in range(n)]
    res=[sum(l[i]) for i in range(n)]
    print("#{} {} {}".format(T+1, res.count(max(res)), max(res)))

#solve same problem 6913