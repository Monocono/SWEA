import sys
sys.stdin = open("./Input_Data/D3/9997.txt","r")

for T in range(int(input())):
    c = int(input())
    print("#{} {} {}".format(T+1, c*2//60,c*2%60))