class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}
        for i in s:
           hmap[i] = hmap.get(i, 0) + 1
        for i in t:
            if i in hmap:
                hmap[i] -= 1
                if hmap[i] == 0:
                    del hmap[i]
            else:
                return False
        return True if hmap == {} else False