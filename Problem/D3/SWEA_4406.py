import sys
sys.stdin = open("./Input_Data/D3/4406.txt","r")

for T in range(int(input())):
    s=str(input())
    print("#{} {}".format
    (T+1, "".join([x for x in s if x not in "aeiou"])))