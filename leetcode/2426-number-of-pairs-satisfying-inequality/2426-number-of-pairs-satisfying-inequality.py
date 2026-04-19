class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        temp =[]
        ans = 0

        for i in range(len(nums1)):
            temp.append(nums1[i] - nums2[i])

        def merge_sort(arr):
            nonlocal ans
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            i = 0
            for j in range(len(right)):
                while i < len(left) and left[i] <= right[j] + diff:
                    i += 1
                ans += i    
            merged = []
            l , r = 0 , 0
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    merged.append(left[l])
                    l += 1
                else:
                    merged.append(right[r])
                    r += 1

            merged.extend(left[l:])
            merged.extend(right[r:])
            return merged
        merge_sort(temp)
        return ans                         

            



        