file_input = input()

dic = {'F':2,'L':6,'S':6,'Y':2,
       'C':2,'W':1,
       'P':4,'H':2,'Q':2,'R':6,
       'I':3,'M':1,'T':4,'N':2,
       'K':2,'V':4,
       'A':4,'D':2,'E':2,'G':4}

total = 3

for i in range(len(file_input)):
    total = (total%1000000)*dic[file_input[i]]

print (total)