# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        seen = {}
        previous = None
        curr = head
        while curr:
            if curr.val in seen:
                #remove here
                curr = curr.next
                prev.next = curr
                continue
            else:
                #add hashmap
                seen[curr.val] = seen.get(curr.val,0) + 1

            prev = curr
            curr = curr.next

        return head

        