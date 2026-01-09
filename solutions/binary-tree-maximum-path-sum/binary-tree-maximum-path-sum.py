# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self, root, maxi):
        if root is None:
            return 0
        ls = max(0, self.f(root.left, maxi))
        rs = max(0, self.f(root.right, maxi))
        ps = root.val + ls + rs
        maxi[0] = max(ps, maxi[0])
        return root.val + max(ls, rs)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = [-inf]
        self.f(root, maxi)
        return maxi[0]