class Solution(object):
    def preorderTraversal(self, root):
        result = []
        
        def dfs(node):
            if node:
                result.append(node.val)
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        return result