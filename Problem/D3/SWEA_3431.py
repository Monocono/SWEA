import sys
sys.stdin = open("./Input_Data/D3/3431.txt","r")

for T in range(int(input())):
    l,u,x = map(int,input().split())
    print("#{} {}".format(T+1, 
    0 if x>=l and x<=u else -1 if x>u else l-x))