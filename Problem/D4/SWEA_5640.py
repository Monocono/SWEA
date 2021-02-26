import sys
sys.stdin = open("./Input_Data/D4/5640.txt","r")

for T in range(int(input())):
    r_l= list(map(int,input().split()))
    s_l=[1,0]; t_l=[0,1]
    r=1
    while r != 0:
        q= r_l[0]//r_l[1]
        r =r_l[0]%r_l[1]
        r_l[0]=r_l[1]
        r_l[1]=r
        s = s_l[0] - q*s_l[1]
        t = t_l[0] - q*t_l[1]
        s_l[0] = s_l[1]
        s_l[1] = s
        t_l[0] = t_l[1]
        t_l[1] = t
    k = r_l[2]//r_l[0]
    print("#{} {} {}".format(T+1, s_l[0]*k, t_l[0]*k))
#https://8iggy.tistory.com/19
#https://ieatt.tistory.com/17