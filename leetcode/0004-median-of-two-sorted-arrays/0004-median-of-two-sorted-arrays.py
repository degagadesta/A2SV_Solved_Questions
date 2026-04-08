class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = 0 
        r = 0
        cnt = 0
        md = (len(nums1) + len(nums2) ) // 2 + 1
        temp = []
        while cnt < md:
            if l >= len(nums1):
                while cnt < md:
                    temp.append(nums2[r])
                    r += 1
                    cnt += 1
                break
            elif r >= len(nums2) :
                while cnt < md:
                    temp.append(nums1[l])
                    l += 1
                    cnt += 1 
                break

            if nums1[l] < nums2[r]:
                temp.append(nums1[l])
                cnt += 1
                l += 1
            else :
                temp.append(nums2[r])
                cnt += 1
                r += 1
        if not (len(nums1) + len(nums2) )% 2 :
            return (temp[-1] + temp[-2]) / 2
        return temp[-1]            

        