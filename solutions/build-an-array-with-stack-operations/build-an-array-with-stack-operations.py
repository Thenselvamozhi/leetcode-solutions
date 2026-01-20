class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        array = []
        temp = []

        j = 0
        for i in range(1, max(target)+1):
            temp.append(i)
            array.append("Push")
            if temp[j] != target[j]:
                array.append("Pop")
                temp.pop()
            else:
                j += 1
        return array
            