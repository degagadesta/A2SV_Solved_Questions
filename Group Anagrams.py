class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp=defaultdict(list)
        for i in range(len(strs)) :
            word=str(sorted(strs[i]))
            temp[word].append(strs[i])
        ans = list(temp.values())
        return ans
            

        
