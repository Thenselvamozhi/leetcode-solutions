class Solution(object):
    def isPalindrome(self, s):
        string = ''
        s = s.lower()
        valid = 'abcdefghijklmnopqrstuvwxyz1234567890'
        for i in s:
            if i in valid:
                string += i
        i, j = 0, len(string)-1
        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True