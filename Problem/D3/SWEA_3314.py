import sys
sys.stdin = open("./Input_Data/D3/3314.txt","r")

for T in range(int(input())):
    l = list(map(int,input().strip().split()))
    for i in range(5):
        if l[i] <40:
            l[i] = 40
    print("#{} {}".format(T+1, sum(l)//len(l)))