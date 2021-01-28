import sys
sys.stdin = open("./Input_Data/D2/1986.txt","r")

for T in range(int(input())):
    a = int(input())
    res = 0
    for i in range(1,a+1):
        if i%2==0:
            res -= i
        else: 
            res+=i
    print("#{} {}".format(T+1, res))