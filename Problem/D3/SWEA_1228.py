import sys
sys.stdin = open("./Input_Data/D3/1228.txt","r")

for T in range(10):
    len_s = int(input())
    s = list(map(int,input().split()))
    len_op = int(input())
    op = list(map(str,input().split()))
    for i in range(len(op)):
        if op[i] == "I":
            for j in range(int(op[i+2])):
                s.insert(int(op[i+1])+j,int(op[i+j+3]))
    print("#{}".format(T+1), end=" ")
    for a in range(10):
        print(s[a],end=" ")
    print()
