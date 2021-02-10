import sys
sys.stdin = open("./Input_Data/D3/9317.txt","r")

for T in range(int(input())):
    n = int(input())
    s1 = str(input())
    s2 = str(input())
    res = 0
    for i in range(n):
        if s1[i] == s2[i]:
            res+=1
    print("#{} {}".format(T+1,res))

    #solve