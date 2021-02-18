import sys
sys.stdin = open("./Input_Data/D3/8931.txt","r")

for T in range(int(input())):
    stack =[]
    for i in range(int(input())):
        t = int(input())
        if t != 0: stack.append(t)
        else: stack.pop()
    print("#{} {}".format(T+1, sum(stack)))
#solve