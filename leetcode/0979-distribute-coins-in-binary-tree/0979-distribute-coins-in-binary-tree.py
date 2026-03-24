# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        temp = 0
        def helper(root):
            nonlocal ans
            if not root :
                return 0
            l_cnt = helper(root.left)
            r_cnt = helper(root.right)    
            ans += abs(l_cnt) + abs(r_cnt)
            
            return root.val - 1 + l_cnt + r_cnt

        ans = 0    
        temp = helper(root)
        return ans    
