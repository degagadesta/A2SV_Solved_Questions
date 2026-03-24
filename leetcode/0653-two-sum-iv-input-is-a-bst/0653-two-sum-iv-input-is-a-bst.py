# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        temp = []
        def helper(root, temp ):
            if not root:
                return 
            helper(root.left, temp)
            temp.append(root.val)
            helper(root.right, temp)
        helper(root, temp)
        ans = False 
        left = 0
        right = len(temp) - 1
        while left < right :
            tot = temp[left] + temp[right]
            if tot == k :
                ans = True
                break
            elif tot < k :
                left += 1
            else :
                right -=1
        return ans                       

        