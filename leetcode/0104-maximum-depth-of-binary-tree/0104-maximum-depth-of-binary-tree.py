# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root, mx_d) :
            nonlocal ans
            if not root:
                ans = max(ans, mx_d)
                return 
            l = helper(root.left, mx_d + 1)
            r = helper(root.right, mx_d + 1) 
            return  
        mx_d = 0
        ans = 0     
        res = helper(root, mx_d)
        return ans