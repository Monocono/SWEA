import sys
sys.stdin=open("./Input_Data/D1/2070.txt","r")

for T in range(int(input())):
    a,b=map(int, input().split(" "))
    res ='=' if a==b else '<' if a<b else '>'
    print("#{} {}".format(T+1, res))