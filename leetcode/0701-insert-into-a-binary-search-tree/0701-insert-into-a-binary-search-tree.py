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
        while temp :
            if temp.val > val :
                if not temp.left :
                    t = TreeNode(val)
                    temp.left = t
                    break
                else:
                    temp = temp.left
            else :
                if not temp.right :
                    t = TreeNode(val)
                    temp.right = t
                    break
                else:
                    temp = temp.right 
        return root                   
        