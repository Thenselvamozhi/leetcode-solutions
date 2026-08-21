class Solution(object):
    def detectCapitalUse(self, word):
        count = 0
        for letter in word:
            if 65 <= ord(letter) <= 90:
                count += 1
        if count == len(word) or count == 0 or (count == 1 and 65 <= ord(word[0]) <= 90):
            return True
        return False