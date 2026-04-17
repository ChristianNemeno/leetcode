# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:


        curr = ListNode()
        curr = head
        prev = head
        
        while curr:
            # edge case for the head
            if head.val == val:
                head = head.next
                curr = head
            elif curr.val == val:
                # deletion 
                prev.next = curr.next
                curr = prev.next
            else:
                # movement
                prev = curr
                curr = curr.next 
        return head
        