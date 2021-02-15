import sys
sys.stdin = open("./Input_Data/D3/8741.txt","r")

for T in range(int(input())):
    l = list(map(str,input().strip().split()))
    s=""
    for i in l:
        s+=i[0]
    print("#{} {}".format(T+1, s.upper()))
#solve