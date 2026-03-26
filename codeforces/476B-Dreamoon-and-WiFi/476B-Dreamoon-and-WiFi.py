def helper(cnt, i):
    global ans, b , point, alll
    if i >= len(a):
        if cnt == point:
            ans += 1
        alll += 1    
        return
    if b[i] == "+":
        helper(cnt + 1, i + 1) 
    elif b[i] == "-":
        helper(cnt - 1, i + 1)
    elif b[i] =="?":
        helper(cnt + 1, i + 1)
        helper(cnt - 1, i+1)  
helper(0,0)
print(f"{ans / alll:.12f}")