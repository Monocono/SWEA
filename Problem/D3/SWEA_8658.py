import sys
sys.stdin = open("./Input_Data/D3/8658.txt","r")

def sum_digit(num):
    return sum(map(int,num))

for T in range(int(input())):
    l= list(map(str,input().split()))
    res= []
    for i in l:
        res.append(sum_digit(i))
    print("#{} {} {}".format(T+1, max(res), min(res)))

#solve