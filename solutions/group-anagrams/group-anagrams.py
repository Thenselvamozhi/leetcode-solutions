class Solution(object):
    def groupAnagrams(self, strs):
        d = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            d.setdefault(sortedWord, []).append(word) #setdefault() - Sets default value to sortedWord(key of the dict) as [], then appends the word as a value for the sortedWord
        ans = []
        for value in d.values(): #d.values() iterates the values of the dictionary
            ans.append(value)
        return ans