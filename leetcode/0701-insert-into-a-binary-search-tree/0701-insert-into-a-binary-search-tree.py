# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root :
            t = TreeNode(val)
            root = t
            return root
        temp = root
        if temp.val > val :
            root.left = self.insertIntoBST(temp.left,val)
        else :
            root.right = self.insertIntoBST(temp.right,val)
   
        return root                   
        