import sys
sys.stdin = open("./Input_Data/D3/7728.txt")

for T in range(int(input())):
    s=set()
    s.update(list(input()))
    print("#{} {}".format(T+1, len(s)))

#solve