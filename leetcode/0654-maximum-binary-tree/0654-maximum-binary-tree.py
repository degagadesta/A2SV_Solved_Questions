# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(temp):
            if not temp:
                return None
            if len(temp) == 1:
                return TreeNode(temp[0])    
            t = TreeNode(max(temp))
            ind = temp.index(t.val)
            t.left = helper(temp[:ind])
            t.right = helper(temp[ind+1:])
            return t

        head = TreeNode(max(nums))
        ind = nums.index(head.val)
        head.left = helper(nums[:ind])
        head.right = helper(nums[ind+1:])
        return head



        