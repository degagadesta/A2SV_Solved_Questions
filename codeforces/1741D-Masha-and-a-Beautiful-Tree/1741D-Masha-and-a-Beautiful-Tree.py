def helper(arr):
        global cnt
        if len(arr) == 2:
            if arr[0] > arr[1]:
                cnt += 1
                arr[0] , arr[1] = arr[1], arr[0]
            return arr
        p = len(arr)
        
        left = helper(arr[:p//2])
        right = helper(arr[p//2 :])
        temp =[]
        if left[-1] < right[-1]:
            temp = left + right
        else: 
            cnt += 1
            temp = right + left
        return temp
    if len(a) == 1 :
        print(0)
    else:    
        temp = helper(a)
        fl = 1
        for i in range(1, n):
            if temp[i] < temp[i-1]:
                fl = 0
                break
        if fl:
            print(cnt)
        else:
            print(-1)