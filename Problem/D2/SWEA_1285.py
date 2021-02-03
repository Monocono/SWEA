import sys
sys.stdin = open("./Input_Data/D2/1285.txt","r")

for T in range(int(input())):
    person = int(input())
    record = list(map(int,input().split()))
    record_dict={}
    min_record = 9999999
    for p in range(person):
        rec = abs(record[p])
        if rec in record_dict:
            record_dict[rec] +=1
        else:
            record_dict[rec] = 1
        if rec < min_record:
            min_record = rec
    print("#{} {} {}".format(T+1,min_record,record_dict.get(min_record)))