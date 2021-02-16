import sys
sys.stdin = open("./Input_Data/D3/9700.txt","r")

for T in range(int(input())):
    p,q = map(float,input().split())
    print('#{} {}'.format(T+1,'YES' if p*(1-q)*q>(1-p)*q else 'NO'))