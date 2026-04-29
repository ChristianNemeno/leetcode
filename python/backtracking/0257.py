# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        if root is None:
            return None
        res = []

        def backtrack(root, path):
            

            path.append(root.val)

            if not root.left and not root.right:
                res.append("->".join(map(str,path)))
                

            if root.left:
                backtrack(root.left, path)
            if root.right:
                backtrack(root.right, path)

            path.pop()

        backtrack(root,[])
        return res