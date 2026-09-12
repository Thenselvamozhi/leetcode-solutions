class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = maxLength = 0
        exists = [False] * 128
        while right < len(s):
            if not exists[ord(s[right])]:
                exists[ord(s[right])] = True
                maxLength = max(maxLength, right-left+1)
                right += 1
            else:
                exists[ord(s[left])] = False
                left += 1
        return maxLength