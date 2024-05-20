# 226. Invert Binary Tree

# root stays the same, but every single children at each level is inverted
#  recursive definition.

class Solution:
    def invertBinaryTree(self, root: TreeNode) -> TreeNode:
        # base case --> if root is null, return null
        if not root:
            return None
        
        # swap children
            # store the left child in temp node
            # store right child in left child
            # store left child in right child
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # now have to recursively invert subtrees.
            # invert the root's right subtree
            # invert the root's left subtree

            # making recursive call in funct. inside.
            # will call the func -> setting subtrees as the root node for each call.
        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)

        
