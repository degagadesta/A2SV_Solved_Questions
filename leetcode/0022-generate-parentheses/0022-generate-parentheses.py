class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(arr):
            st = []
            for op in arr:
                if op == "(":
                    st.append(op)
                else:
                    if not st:
                        return False
                    st.pop()
            return not st                
        arr = ["_"] * (2*n)
        ans = []
        def backtrack(i):
            if i == 2*n:
                if arr and isValid(arr):
                    ans.append("".join(arr))
                return 
            arr[i] ="("
            backtrack(i+1)
            arr[i] = (")")
            backtrack(i+1)
            arr[i] = "_"
        backtrack(0) 
        return ans           
        