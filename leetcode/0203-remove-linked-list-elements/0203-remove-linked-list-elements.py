# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        temp = head.next
        prev = head
        while temp :
            if temp.val == val :
                prev.next = temp.next
                temp = temp.next
                continue
            temp = temp.next
            prev = prev.next

        return head.next        
        