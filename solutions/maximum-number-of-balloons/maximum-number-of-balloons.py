class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {}
        for char in text:
            count[char] = count.get(char, 0) + 1

        string = ['b', 'a', 'n']
        print(count)

        if ('l' in count and 'o' in count):
            count['l'] //= 2
            count['o'] //= 2
            minfreq = min(count['l'], count['o'])
        else:
            return 0

        for ch in string:
            if ch not in count:
                return 0
            minfreq = min(minfreq, count[ch])
        return minfreq