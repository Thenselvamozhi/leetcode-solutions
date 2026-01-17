class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''
        i = 0
        char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"

        while i < len(s):
            if s[i] in char:
                string += s[i]
            i+=1

        if not string:
            return True
        string = string.lower()

        i, j = 0, len(string)-1
        while i<j:
            if string[i] == string[j]:
                i += 1
                j -= 1
            else:
                return False
        return True