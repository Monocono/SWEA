import sys
sys.stdin = open("./Input_Data/D3/5162.txt","r")

for T in range(int(input())):
    a,b,c= map(int,input().split())
    print("#{} {}".format(T+1, c//b if a>b else c//a))