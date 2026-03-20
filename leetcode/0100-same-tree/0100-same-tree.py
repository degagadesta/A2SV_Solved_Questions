# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque()
        q2 = deque()
        if (not p and q ) or p and not q:
            return False
        if p and q :
            if p.val != q.val :
                return False
            q1.append(p)
            q2.append(q)  
            while q1 and q2 :
                if len(q1) != len(q2) :
                    return False
                n = len(q1)
                for i in range(n) :
                    t1 = q1.popleft()
                    t2 = q2.popleft()
                    if (t1.left and (not t2.left)) or (t2.right and (not t1.right)) or ((not t1.left) and t2.left) or ((not t2.right) and t1.right)  :
                        return False
                    if (t1.left and t2.left and t1.left.val != t2.left.val )or (t1.right and t2.right and t1.right.val != t2.right.val ):
                        return False     
                    if t1.left :
                        q1.append(t1.left)
                        q2.append(t2.left)
                    if t1.right :
                        q1.append(t1.right)
                        q2.append(t2.right)
        return len(q1) == len(q2)                                   
        