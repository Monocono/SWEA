import sys
sys.stdin = open("./Input_Data/D2/1946.txt", "r")

for T in range(int(input())):
    n = int(input())
    s=""
    for i in range(n):
        Ci, Ki = input().split()
        for idx in range(int(Ki)):
            s+=Ci
    cnt = 1
    print("#{}".format(T+1))
    for i in s:
        print(i,end="")
        if cnt % 10 == 0:
            print()
        cnt+=1
    print()
