# 617. Merge Two Binary Trees

# will use recursive definition

# Definition for a binary tree node
# class TreeNode:
    # def __init__(self, vall = 0, Left = None, right = None):
#         self.val = val
#         self.Left = left
#         self.Right = right

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # base case --> if both are Null
        if not t1 and not t2:
            return None
        
        v1 = t1.val if t1 else 0
        v2 = t2.val if t2 else 0 
        root = TreeNode(v1 + v2)

        root.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        root.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)

        return root
    
    # O(n + m) time complexity