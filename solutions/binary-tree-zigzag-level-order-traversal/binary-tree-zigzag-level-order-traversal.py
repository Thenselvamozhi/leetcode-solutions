# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        q = deque()
        q.append(root)
        l = 0
        while len(q) > 0:
            s = len(q)
            temp = []
            for _ in range(s):
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if l % 2 == 1:
                temp.reverse()
            ans.append(temp)
            l += 1
        return ans