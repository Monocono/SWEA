import sys
sys.stdin = open("./Input_Data/D3/1213.txt","r")

for T in range(10):
    n =int(input())
    t = str(input())
    s=str(input())
    print("#{} {}".format(n,s.count(t)))