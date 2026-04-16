# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")
        mn = 0
        def helper(temp):
            nonlocal ans, mn
            if not temp:
                return 0 
            leftm = max(0, helper(temp.left))
            rightm = max(0, helper(temp.right))
            ans = max(ans, temp.val+rightm + leftm)
            return temp.val + max(rightm ,leftm)
        helper(root)     
        return ans  



        