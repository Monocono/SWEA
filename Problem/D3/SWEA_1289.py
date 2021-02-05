import sys
sys.stdin = open("./Input_Data/D3/1289.txt","r")

for T in range(int(input())):
    l = input()
    flag = "0"
    res = 0
    for i in range(len(l)):
        if l[i] != flag:
            res+=1
            flag=l[i]
    print("#{} {}".format(T+1, res))