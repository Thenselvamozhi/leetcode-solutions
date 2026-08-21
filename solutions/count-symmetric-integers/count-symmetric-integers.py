class Solution(object):
    def countSymmetricIntegers(self, low, high):
        count = 0
        for i in range(low, high+1):
            i = str(i)
            if len(i) % 2 == 0:
                first_half, second_half = 0, 0
                length = len(i) / 2
                for n in range(length):
                    first_half += int(i[n])
                for n in range(length, len(i)):
                    second_half += int(i[n])
                if first_half == second_half:
                    count += 1
        return count