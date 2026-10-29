class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
            
        complements = set()
        a ,b = 0, 0

        while (a*a) < c:
            complement = c - (a*a)
            complements.add(complement)
            a+=1
        
        while (b*b) <= c:
            if (b*b) in complements:
                return True
            b += 1

        return False 
        

