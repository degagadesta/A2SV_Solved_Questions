class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def helper(idx, nums, temp):
            # Same base case
            if idx >= len(num):
                return len(temp) >= 3 and not nums
            
            nums.append(num[idx])
            
            if not (len(nums) > 1 and nums[0] == "0"):
                
                current_val = int("".join(nums))
                
                is_valid_sum = True
                if len(temp) >= 2:
                    expected = int("".join(temp[-2])) + int("".join(temp[-1]))
                    if current_val != expected:
                        is_valid_sum = False
                
                if is_valid_sum:
                    temp.append(nums.copy())
                    if helper(idx + 1, [], temp):
                        return True
                    temp.pop() 
                
                
                if len(temp) >= 2:
                    expected = int("".join(temp[-2])) + int("".join(temp[-1]))
                    if current_val < expected:
                        if helper(idx + 1, nums, temp):
                            return True
                else:
                    if helper(idx + 1, nums, temp):
                        return True
            
            nums.pop()
            return False      

        return helper(0, [], [])
