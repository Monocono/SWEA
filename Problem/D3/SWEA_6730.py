import sys
sys.stdin = open("./Input_Data/D3/6730.txt", "r")

for T in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    up= [0];down = [0]
    for i in range(n-1):
        if l[i] < l[i+1]: up.append(l[i+1]-l[i])
        else: down.append(l[i]-l[i+1])
    print("#{} {} {}".format(T+1,max(up),max(down)))

#output 

#1 60 40
#2 70 0
#3 0 80
#4 0 0
#5 333 878