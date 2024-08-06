# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        result = []
        def dfs(node):
            if node is not None:
                dfs(node.left)
                dfs(node.right)
                result.append(node.val)
        dfs(root)
        return result

        