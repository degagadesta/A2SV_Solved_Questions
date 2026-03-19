# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        qu = deque()
        tot = 0
        qu.append(root)
        while qu:
            n = len(qu)
            for _ in range(n) :
                temp = qu.popleft()
                if temp.val % 2 == 0 :
                    if temp.left  :
                        if temp.left.left :
                            tot += temp.left.left.val
                        if temp.left.right :
                            tot += temp.left.right.val
                    if temp.right :
                        if temp.right.left :
                            tot += temp.right.left.val
                        if temp.right.right :
                            tot += temp.right.right.val
                if temp.left :
                    qu.append(temp.left)
                if temp.right :
                    qu.append(temp.right) 
        return tot                            
                                   
        