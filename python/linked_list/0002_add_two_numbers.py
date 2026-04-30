# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNod    e]
        """
        carry = 0
        digit = 0

        dummy = ListNode()
        current = ListNode()
        dummy.next = current
        while l1 or l2 or carry:
            adding = carry            
            if l1:
                adding += l1.val
            if l2:
                adding += l2.val

            digit = adding % 10
            carry = adding // 10
            
            add = ListNode(digit)
            current.next = add 
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        

        return dummy.next.next