class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        temp = {
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p","q","r","s"],
            "8" : ["t","u","v"],
            "9" : ["w","x","y","z"]
        }
        ans = []
        def backtrack(i,comb):
            if len(comb) == len(digits) :
                ans.append("".join(comb))
                return 
            for j in range(len(temp[digits[i]])) :
                comb.append(temp[digits[i]][j])
                backtrack(i+1, comb)
                comb.pop()
        ans = []        
        backtrack(0, [])
        return ans            
            
        