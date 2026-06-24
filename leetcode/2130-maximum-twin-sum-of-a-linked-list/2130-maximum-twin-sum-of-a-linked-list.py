# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        n = len(temp)
        res = 0
        for i in range(n // 2):
            res = max(res, temp[i] + temp[n - i -1])
        return res        