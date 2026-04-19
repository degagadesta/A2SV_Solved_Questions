class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        cnt  = [0] * len(nums)
        n = [[val , ind] for (ind , val) in enumerate(nums)]
        def merge(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge(arr[:mid])
            right = merge(arr[mid:])

            r = 0
            for l in range(len(left)):
                while r < len(right) and left[l][0] > right[r][0] :
                    r += 1
                cnt[left[l][1]] += r
            return sorted(left + right)
        merge(n)
        return cnt                
        