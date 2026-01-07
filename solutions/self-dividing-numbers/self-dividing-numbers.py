class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        sol = []
        for i in range(left, right+1):
            n = str(i)
            flag = True
            for j in n:
                if (int(j) == 0) or ((i % int(j)) != 0):
                    flag = False
                    break
            if flag == True:
                sol.append(i)
        return sol