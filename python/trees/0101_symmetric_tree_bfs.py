# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        queue = deque([root.left, root.right])


        while queue: 
            l = queue.popleft()
            r = queue.popleft()

            if not l and not r: 
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            

            queue.append(l.left)
            queue.append(r.right)
            queue.append(l.right)
            queue.append(r.left)

        return True