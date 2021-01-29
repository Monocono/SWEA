import sys
sys.stdin = open("./Input_Data/D2/1984.txt","r")

for T in range(int(input())):
    l = list(map(int,input().split()))
    l.pop(l.index(max(l))); l.pop(l.index(min(l)))
    print("#{} {}".format(T+1, round(sum(l)/len(l))))