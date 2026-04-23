# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if  not root:
            return []
        ans = []
        queue = deque()
        queue.append(root)
        
        while queue:
            ans.append([node.val for node in queue])
            n = len(queue)
            for i in range(n):
                j = queue.popleft()
                if j.left:
                    queue.append(j.left)
                if j.right:
                    queue.append(j.right)
        return ans    

        