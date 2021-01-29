import sys
sys.stdin = open("./Input_Data/D2/1974.txt","r")

nums= set((1,2,3,4,5,6,7,8,9))
def solve(puzzle):
    for i in range(9):
        if set(puzzle[i]) != nums:
            return 0
        col=set()
        col.clear()
        for j in range(9):
            col.add(puzzle[j][i])
        if col != nums:
            return 0
    
    pix=set()
    for a in range(0,7,3):
        for b in range(0,7,3):
            pix.clear()
            for c in range(3):
                for d in range(3):
                    pix.add(puzzle[a+c][b+d])
            if pix != nums:
                return 0
    return 1


for T in range(int(input())):
    puz=[]
    for i in range(9):
        row=list(map(int,input().split()))
        puz.append(row)
    print("#{} {}".format(T+1, solve(puz)))