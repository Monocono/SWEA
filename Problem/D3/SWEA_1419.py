import sys
sys.stdin = open("./Input_Data/D3/1419.txt","r")

for T in range(int(input())):
    n,a,b = map(int,input().split())
    res = 99999999
    for r in range(1,int(n**(0.5))):
        k = n//r
        for c in range(1,k):
            t = a*abs(r-c) + b*(n-r*c)
            if t < res:
                res = t
    print("#{} {}".format(T+1, res))

    '''
    a * abs(r-c) + b * (n-r*c) >= 0
    i) a * abs(r-c)가 최소가 되는경우 
    => abs(r-c)가 0이 되는 경우이므로 r - c = = 0 
    ∴ r = c
    ii) b * (n-r*c)가 최소가 되는경우
    => n-r*c 가 0이 되는 경우 이므로 n = r * c
    => i) 식에 따라 n = r^2
    ∴ r = sqrt(n) , c = n//r
    '''