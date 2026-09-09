class Solution(object):
    def uniqueMorseRepresentations(self, words):
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans = set()
        for word in words:
            decode = ""
            for letter in word:
                decode += codes[ord(letter) - 97]
            ans.add(decode)
        return len(ans)