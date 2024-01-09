# Beats 99.58% of users with Python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root.val < low:
            return self.rangeSumBST(root.right, low, high) if root.right else 0
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high) if root.left else 0
        else:
            left_sum = self.rangeSumBST(root.left, low, high) if root.left else 0
            right_sum = self.rangeSumBST(root.right, low, high) if root.right else 0
            return left_sum + root.val + right_sum