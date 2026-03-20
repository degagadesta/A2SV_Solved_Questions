# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper (p , q) :
            if not p and not q :
                return True
            if (p and not q )or(not p  and q) :
                return False
            if p.val != q.val :
                return False    
            return helper(p.left, q.left) and helper(p.right, q.right)         
        queue = deque()
        queue.append(root)
        while queue :
            temp = queue.popleft()
            if temp.val == subRoot.val :
                ans = helper(temp, subRoot) 
                if ans :
                    return ans
            if temp.left :
                queue.append(temp.left)
            if temp.right :
                queue.append(temp.right)
        return False                                   
        