import sys
sys.stdin = open("./Input_Data/D2/1940.txt","r")

for T in range(int(input())):
    sec = int(input())
    distance = 0; speed = 0
    for ms in range(sec):
        op = list(map(int,input().split()))
        if op[0] == 1:
            speed += op[1]
        elif op[0] == 2:
            if speed < op[1]:
                speed = 0
            else:
                speed-=op[1]
        distance += speed
    print("#{} {}".format(T+1, distance))