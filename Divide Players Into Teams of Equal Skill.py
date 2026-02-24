class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        total = sum(skill)
        if n == 2:
            return skill[0] * skill[1]
        left = 0
        right = n-1
        ans = 0  
        exp = total // (n//2)
        skill.sort()
        while left < right :
            if skill[left] + skill[right] == exp :
                ans += (skill[left] * skill[right] ) 
                left += 1
                right -= 1 
            else:
                return -1
        return ans            
