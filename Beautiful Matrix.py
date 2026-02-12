arr =[]
for i in range(5):
    temp = list(map(int,input().split()))
    arr.append(temp)
    cnt = temp.count(1)
    
    if cnt == 1 :
        column = temp.index(1)
        row = i
print (abs(2 - row) + abs(2 - column))        
            
