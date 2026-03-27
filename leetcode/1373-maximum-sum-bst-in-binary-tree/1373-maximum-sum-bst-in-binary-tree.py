# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            nonlocal ans
            if not root:
                return 0, True, float("-inf"), float("inf")
            suml, isBstl, maxLeftl, minRightl = helper(root.left)
            sumr, isBstr, maxLeftr, minRightr = helper(root.right)
            if isBstl and isBstr and maxLeftl < root.val < minRightr :
                total = suml + sumr + root.val
                ans = max(ans, total)
                return total, True, max(maxLeftr, root.val), min(minRightl, root.val)
            return 0 , False , float("-inf"), float("inf")  
        ans = 0
        helper(root)
        return ans      



        