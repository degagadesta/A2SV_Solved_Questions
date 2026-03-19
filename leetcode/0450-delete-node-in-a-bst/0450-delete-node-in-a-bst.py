# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def helper( root, key):
            if not root :
                return root
        
            if root.val > key :
                root.left = helper(root.left,key)
            elif root.val < key  :
                root.right = helper( root.right,key)
            else:
                if not root.left :
                    return root.right
                elif not root.right :
                    return root.left

                temp = root.left
                prev = None
                while temp.right:
        
                    temp = temp.right
                root.val = temp.val
                root.left = helper(root.left, temp.val)
            return root    








            #     if not parent :
            #         return None

                
            #     if parent.left == root :
            #         if not root.left and not root.right :
            #             parent.left = None
            #             return parent
            #         t = root.left
            #         prev = None
            #         while t.right :
            #             prev = t
            #             t = t.right
            #         parent.left.val = t.val
            #         prev.right = t.left
                    
            #     else:
            #         if not root.left and root.right :
            #             parent.right = None
            #             return parent
            #         t = temp.left
            #         prev = None
            #         while t.right :
            #             prev = t
            #             t = t.right
            #         parent.right.val = t.val
            #         prev.right = t.left
            #     return parent  
            # return root      


        parent = None
        return helper( root,key)        

            