class Solution(object):
    def fizzBuzz(self, n):
        ans = []
        for i in range(1, n+1):
            string = ""
            if i % 3 == 0:
                string += "Fizz"
            if i % 5 == 0:
                string += "Buzz"
            if len(string):
                ans.append(string)
            else:
                ans.append(str(i))
        return ans