import sys
sys.stdin = open("./Input_Data/D4/1824.txt","r")

def solve():
    dx = [-1,0,1,0] # 북동남서 0123
    dy = [0,1,0,-1]
    visit = [[[[0 for _ in range(16)] for _ in range(4)]for _ in range(20)]for _ in range(20)]
    stack = [[0,0,1,0]]
    while stack:
        x,y,dir,mem = stack.pop()
        if visit[x][y][dir][mem]:
            continue
        else:
            visit[x][y][dir][mem] = True
            if code[x][y] == '^' or (code[x][y] =='|' and mem != 0): stack.append([(x+dx[0])%r,(y+dy[0])%c,0,mem])
            elif code[x][y] == '>' or (code[x][y] == '_' and mem == 0): stack.append([(x+dx[1])%r,(y+dy[1])%c,1,mem])
            elif code[x][y] == 'v' or (code[x][y] == '|' and mem == 0): stack.append([(x+dx[2])%r,(y+dy[2])%c,2,mem])
            elif code[x][y] == '<' or (code[x][y] =='_' and mem !=0): stack.append([(x+dx[3])%r,(y+dy[3])%c,3,mem])
            elif code[x][y] == '+': stack.append([(x+dx[dir])%r,(y+dy[dir])%c,dir,(mem+1)%16])
            elif code[x][y] == '-': stack.append([(x+dx[dir])%r,(y+dy[dir])%c,dir, mem-1 if mem!=0 else 15])
            elif code[x][y] == '.': stack.append([(x+dx[dir])%r,(y+dy[dir])%c,dir,mem])
            elif code[x][y] == '?':
                for i in range(4):
                    stack.append([(x+dx[i])%r,(y+dy[i])%c,i,mem])
            elif code[x][y] == '@': return True
            else:
                stack.append([(x+dx[dir])%r,(y+dy[dir])%c,dir,int(code[x][y])])
    return False

for T in range(int(input())):
    r,c= map(int,input().split())
    code=[input() for _ in range(r)]
    print("#{} {}".format(T+1, 'YES' if solve() else 'NO'))

# https://www.techiedelight.com/depth-first-search/