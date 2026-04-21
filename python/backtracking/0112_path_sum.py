# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        def dfs(root, remain):
            if root is None:
                return False
            
            remain -= root.val
            if root.left is None and root.right is None: 
                return remain == 0
            
            if dfs(root.left, remain):
                return True
            
            if dfs(root.right, remain):
                return True
            
            return False

        return dfs(root, targetSum)
        