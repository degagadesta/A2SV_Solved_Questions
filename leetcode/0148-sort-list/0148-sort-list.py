# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        t = []
        if temp == None :
            return head
        while temp != None :
            t.append(temp.val)
            temp = temp.next
        t.sort()
        temp = head
        i = 0
        while temp  != None :
            temp.val = t[i]
            i += 1
            temp = temp.next    

        return head            
        