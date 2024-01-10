def get_leaves(tree):
    if not tree:
        return []
    
    if (tree.left == None) and (tree.right == None): # if leaf
        return [tree.val]
    else:
        return get_leaves(tree.left) + get_leaves(tree.right)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        print("root1", get_leaves(root1))
        print("root2", get_leaves(root2))
        return get_leaves(root1) == get_leaves(root2)
