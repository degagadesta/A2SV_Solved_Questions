t = int(input())

for _ in range(t) :
    s = input()
    
    i = 0
    temp = set()
    while i < len(s):
        if i < len(s) - 1 and s[i] == s[i+1]:
            i += 2
        else:
            temp.add(s[i])
            i += 1
    ans = list(temp)
    ans.sort()
    print("".join(ans))         
