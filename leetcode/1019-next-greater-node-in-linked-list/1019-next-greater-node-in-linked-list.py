# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        temp = []
        t = head 
        prev = None 
        while t :
            nxt = t.next
            t.next = prev
            prev = t
            t = nxt
        t = prev    
        st = []
        while t :
            while st and st[-1] <= t.val :
                st.pop()
            temp.append(st[-1] if st else 0)
            st.append(t.val)
            t = t.next 
        temp.reverse()    
        return  temp 

        