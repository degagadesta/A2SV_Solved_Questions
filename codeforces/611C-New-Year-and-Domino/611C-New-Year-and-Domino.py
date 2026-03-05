h, w = map(int, input().split())
grid = []
for _ in range(h):
    grid.append(input())

pref_hor = [[0] * (w + 1) for _ in range(h + 1)]
for i in range(h):
    for j in range(1, w):
        val = 1 if grid[i][j] == '.' and grid[i][j-1] == '.' else 0
        pref_hor[i+1][j+1] = pref_hor[i][j+1] + pref_hor[i+1][j] - pref_hor[i][j] + val

pref_ver = [[0] * (w + 1) for _ in range(h + 1)]
for i in range(1, h):
    for j in range(w):
        val = 1 if grid[i][j] == '.' and grid[i-1][j] == '.' else 0
        pref_ver[i+1][j+1] = pref_ver[i][j+1] + pref_ver[i+1][j] - pref_ver[i][j] + val

q = int(input())
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    
    res_h = 0
    if c1 < c2:
        res_h = pref_hor[r2][c2] - pref_hor[r1-1][c2] - pref_hor[r2][c1] + pref_hor[r1-1][c1]
    
    res_v = 0
    if r1 < r2:
        res_v = pref_ver[r2][c2] - pref_ver[r1][c2] - pref_ver[r2][c1-1] + pref_ver[r1][c1-1]
        
    print(res_h + res_v)