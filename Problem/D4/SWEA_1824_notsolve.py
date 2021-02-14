import sys
sys.stdin = open("./Input_Data/D4/1824.txt","r")

dx = [-1,0,1,0]
dy = [0,1,0,-1]
visit = [[[[0 for _ in range(16)] for _ in range(4)]for _ in range(20)]for _ in range(20)]
mem = 0

def solve(x,y,dir,dep):
    res = False
    global mem, r, c
    if '0'<= code[x][y] and code[x][y] <='9': mem = code[x][y]-'0'
    elif code[x][y] =='>' or (code[x][y] =='_' and mem == 0): dir = 0
    elif code[x][y] == 'v' or (code[x][y] == '|' and mem == 0) : dir = 1
    elif code[x][y] =='<' or code[x][y] =='_': dir == 2
    elif code[x][y] =='^' or code[x][y] =='|': dir == 3
    elif code[x][y] =='+': mem = (mem+1) % 16
    elif code[x][y] =='-' and mem == 0: mem == 15
    elif code[x][y] == '-': mem-=1
    elif code[x][y] =='@': return True

    if visit[x][y][dir][mem] == 1: return False
    else: visit[x][y][dir][mem] = 1




for T in range(int(input())):
    r,c= map(int,input().split())
    code=[input() for _ in range(r)]
    print("#{} {}".format(T+1, 'YES' if solve(0,0,0,0) else 'NO'))