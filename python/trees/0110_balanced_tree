# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# sir serats but O(n^2) because we are calculating height for each node and height is O(n) in worst case
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True

        if abs(self.checkHeight(root.right) - self.checkHeight(root.left)) > 1:
            return False
        

        return self.isBalanced(root.left) and self.isBalanced(root.right)

        
    def checkHeight(self, root):
        if root is None:
            return 0

        return 1 + max(self.checkHeight(root.left), self.checkHeight(root.right))

        
# this is O(n)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(root):
            if root is None:
                return True, 0
            
            left_bal , left_h = dfs(root.left)
            right_bal, right_h = dfs(root.right)

            height = 1 + max(left_h, right_h)
            balanced = left_bal and right_bal and abs(left_h - right_h) <= 1

            return balanced, height

        return dfs(root)[0]
        
