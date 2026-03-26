# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def helper(root, comb):
            nonlocal ans
            if not root:
                return 
            n = len(comb)
            for i in range(n):
                comb[i] += root.val
                if comb[i] == targetSum :
                    ans += 1

            comb.append(root.val)
            if root.val == targetSum:
                ans += 1

            helper(root.left, comb)
            helper(root.right, comb)
            n = len(comb)
            for i in range(n):
                comb[i] -= root.val
            comb.pop()
        ans = 0
        helper(root, [])
        return ans                
        