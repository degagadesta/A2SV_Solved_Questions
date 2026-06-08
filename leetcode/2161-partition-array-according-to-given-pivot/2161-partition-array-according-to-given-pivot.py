class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        cnt = 0
        for num in  nums:
            if num == pivot:
                cnt += 1
            elif num < pivot:
                left.append(num)
            else:
                right.append(num)  
        while cnt > 0:
            left.append(pivot)
            cnt -= 1
        left.extend(right)
        return left                            
        