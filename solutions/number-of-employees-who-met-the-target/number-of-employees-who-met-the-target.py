class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        if max(hours) < target:
            return count
        for work in hours:
            if work >= target:
                count += 1
        return count