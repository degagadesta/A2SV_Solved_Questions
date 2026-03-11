# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st = []
        temp = head
        while temp :
            while st and temp.val > st[-1] :
                st.pop()
            st.append(temp.val)
            temp = temp.next
        st.reverse() 
        head = None   
        for i in range(len(st)) :
            n = ListNode(st[i], head)
            head = n
        return head    



        