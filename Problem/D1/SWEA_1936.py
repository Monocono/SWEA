import sys
sys.stdin=open("./Input_Data/D1/1936.txt")

a, b = map(int, input().split())
if (b-a == 1 or b-a==-2):
    print("B")
else:
    print("A")