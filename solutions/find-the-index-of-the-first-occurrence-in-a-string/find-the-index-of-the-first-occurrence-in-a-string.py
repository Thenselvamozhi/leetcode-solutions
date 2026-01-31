class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            j = 0
            if haystack[i] == needle[j]:
                print(i)
                k, flag = i, 1
                while j < len(needle):
                    if haystack[k] == needle[j]:
                        k += 1
                        j += 1
                    else:
                        print(j)
                        flag = 0
                        break
                if flag == 1:
                    return i
        return -1