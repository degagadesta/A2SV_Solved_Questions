# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def  helper(root, comb,summ):
            if not root:
                return
            summ += root.val
            comb.append(root.val)     
            if not root.left and not root.right and summ == targetSum:
                    ans.append(comb.copy())
            helper(root.right, comb,summ)
            helper(root.left, comb,summ)  
            comb.pop()
        ans = []
        helper(root, [],0)
        return ans               
        