class Solution(object):
    def mostWordsFound(self, sentences):
        maximum = -1
        for sentence in sentences:
            words = 1
            for i in sentence:
                if i == ' ':
                    words += 1
            maximum = max(maximum, words)
        return maximum