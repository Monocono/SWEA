import sys
sys.stdin = open("./Input_Data/D3/1208.txt","r")

for T in range(10):
    dump = int(input())
    box = list(map(int,input().strip().split()))
    top = [0 for _ in range(101)]

    for i in range(len(box)):
        top[box[i]] += 1
    min_value = min(box)
    max_value = max(box)
    while dump > 0 and min_value < max_value:
        top[min_value] -= 1
        top[min_value+1] += 1
        top[max_value] -=1
        top[max_value-1] +=1
        if top[min_value] == 0: min_value+=1
        if top[max_value] == 0: max_value-=1
        dump -=1
    print("#{} {}".format(T+1, max_value - min_value))