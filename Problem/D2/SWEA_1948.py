import sys
sys.stdin = open("./Input_Data/D2/1948.txt", "r")

m = [0,31,28,31,30,31,30,31,31,30,31,30,31]

for T in range(int(input())):
    m1,d1,m2,d2 = map(int,input().split())
    print("#{}".format(T+1), end=" ")
    if m1 == m2:
        print(d2-d1+1)
    else:
        print(sum(m[m1:m2],d2)-d1+1)