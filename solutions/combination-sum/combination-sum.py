class Solution:
    def f(self, i, target, arr, temp, ans):
        if target == 0:
            ans.append(list(temp))
            return
        if i == len(arr) or target < 0:
            return
        temp.append(arr[i]) #pick
        self.f(i, target - arr[i], arr, temp, ans)
        temp.pop() #Backtracking -> Undo the pick
        self.f(i+1, target, arr, temp, ans)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        temp = []
        self.f(0, target, nums, temp, ans)
        return ans