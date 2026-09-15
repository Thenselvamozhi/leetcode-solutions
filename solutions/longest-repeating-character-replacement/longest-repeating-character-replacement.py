class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = maxWindow = maxValue = 0
        hashMap = {}
        while right < len(s):
            hashMap[s[right]] = hashMap.get(s[right], 0) + 1
            maxValue = max(maxValue,  hashMap[s[right]])
            if (right - left + 1) - maxValue > k:
                hashMap[s[left]] -= 1
                left += 1
            else:
                maxWindow = max(maxWindow, (right - left + 1))
            right += 1
        return maxWindow