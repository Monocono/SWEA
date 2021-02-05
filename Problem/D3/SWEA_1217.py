import sys
sys.stdin = open("./Input_Data/D3/1217.txt","r")

def solve(n,m):
    if m == 0: return 1
    else: return (solve(n,m-1)*n)
for T in range(10):
    case_num = int(input())
    n,m = map(int,input().split())
    print("#{} {}".format(case_num, solve(n,m)))