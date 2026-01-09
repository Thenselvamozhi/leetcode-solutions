# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self, root):
        if root is None:
            return 0
        lh = self.f(root.left)
        rh = self.f(root.right)

        return 1 + max(lh, rh)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        h = self.f(root)
        return h