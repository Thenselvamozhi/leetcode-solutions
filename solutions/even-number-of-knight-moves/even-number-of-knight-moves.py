class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        return True if (start[0] + start[1]) % 2 == (target[0] + target[1]) % 2 else False