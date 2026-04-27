# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        
        if head is None:
            return head
        
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        
        k = k % length
        for i in range(k):
            tail = head
            prev = tail
            while tail.next:
                prev = tail
                tail = tail.next
                
            tail.next = head
            head = tail
            prev.next = None

        return head

        # not optimal like so slow this