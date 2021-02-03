import sys
sys.stdin=open("./Input_Data/D2/1945.txt","r")

for T in range(int(input())):
    n=int(input())
    nums=[2,3,5,7,11]
    res = []
    for i in nums:
        cnt = 0
        while True:
            if n%i == 0:
                n=n/i
                cnt+=1
            else:
                res.append(str(cnt))
                break
    print("#{} {}".format(T+1," ".join(res)))