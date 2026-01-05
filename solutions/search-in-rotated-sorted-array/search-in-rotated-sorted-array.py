class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo,hi=0,len(nums)-1
        while lo<=hi:
            mid=(lo+hi)//2
            if nums[mid]==target:
                return mid
            elif nums[lo]<=nums[mid]:
                if target>=nums[lo] and target<nums[mid]:
                    #verifying that the target is in the left half
                    hi = mid-1
                else:
                     #target at right half
                    lo=mid+1
            else:
                if target>nums[mid] and target<=nums[hi]: #answer is in right half 
                    lo=mid+1
                else:
                    hi = mid -1
        return -1