class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        n = len(instructions)
      
        ls = [0] * n
        gt = [0] * n
        
        it = [[val, i] for i, val in enumerate(instructions)]

        def merge_sort(l, r):
            if l >= r:
                return
            
            mid = (l + r) // 2
            merge_sort(l, mid)
            merge_sort(mid + 1, r)
            
            i = l
            j = l  
            for k in range(mid + 1, r + 1):
                while i <= mid and it[i][0] < it[k][0]:
                    i += 1
                while j <= mid and it[j][0] <= it[k][0]:
                    j += 1
                
                ls[it[k][1]] += (i - l)
                gt[it[k][1]] += (mid - j + 1)
            
            it[l:r+1] = sorted(it[l:r+1])

        merge_sort(0, n - 1)
        
        ans = sum(min(ls[i], gt[i]) for i in range(n))
        return ans % (10 ** 9 + 7)
