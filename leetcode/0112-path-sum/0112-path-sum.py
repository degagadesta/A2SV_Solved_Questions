# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root,summ):
            if not root:
                return False
            if not root.left and not root.right:
                return summ + root.val == targetSum
            res1 = helper(root.left,summ+root.val)        
            res2 = helper(root.right, summ+root.val) 
            return res1 or res2
        if root:       
            ans = helper(root, 0) 
            return ans    
        else:
            return False       

        