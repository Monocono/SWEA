import sys
sys.stdin= open("./Input_Data/D1/2050.txt","r")

init = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
a=str(input());a.upper()
for i in range(len(a)):
    for j in range(len(init)):
        if a[i] == init[j]:
            print(j+1, end=' ')