import sys
sys.stdin = open("./Input_Data/D3/10570.txt","r")

def is_palindrome(w):
    if w == w[::-1]:
        return True
    return False
    
for T in range(int(input())):
    a,b = map(int,input().split())
    res = 0
    for i in range(a,b+1):
        j = i**(1/2)
        if j == int(j):
            if is_palindrome(str(i)) and is_palindrome(str(int(j))):
                res+=1
    print("#{} {}".format(T+1, res))