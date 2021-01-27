import sys
sys.stdin = open("./Input_Data/D2/1983.txt","r")

grade=['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for T in range(int(input())):
    n, k = map(int,input().split(" "))
    scores=[]
    for i in range(n):
        a,b,c = map(int,input().split())
        sc=a*0.35+b*0.45+c*0.2
        scores.append(sc)
    
    k_score = scores[k-1]
    scores.sort(reverse=True)
    rank = scores.index(k_score)//(n//10)
    print("#{} {}".format(T+1, grade[rank]))
