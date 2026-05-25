class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n-1] == "1":
            return False
        queue = deque([0])
        right = 0
        while queue:
            ind = queue.popleft()
            if ind == n-1:
                return True
            cur_l = ind + minJump
            cur_r = ind + maxJump
            for j in range(max(right+1, cur_l), min(n, cur_r+1)):
                if s[j] == "0":
                    queue.append(j)
            right = max(right, cur_r)
        return False                 

        