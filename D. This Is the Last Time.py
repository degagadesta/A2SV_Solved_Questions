t = int(input())

for _ in range(t):
    n , k = map(int, input().split())
    temp = []
    for i in range(n):
        x,y,z= map(int,input().split())
        temp.append([x,y,z])
    temp.sort(key = lambda item : item[2])
    for i in range(len(temp)):
        if temp[i][0] <= k and temp[i][1] >= k:
              if temp[i][0] <= temp[i][2] and temp[i][1] >= temp[i][2] :
                  k = max(k,temp[i][2])
    print(k)              
                   
    
