# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.result = 1
        
        self.postOrder(root)
        
        return self.result - 1
        
    def postOrder(self, root):
        if not root:
            return 0
        
        left = self.postOrder(root.left)
        right = self.postOrder(root.right)
        
        self.result = max(self.result, (left + right + 1)) # saving current highest node
        
        return max(right,left) + 1
