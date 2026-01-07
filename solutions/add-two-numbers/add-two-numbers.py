# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        temp = ans
        rem = 0
        tempA, tempB = l1, l2
        while tempA or tempB or rem:
            v1 = tempA.val if tempA else 0
            v2 = tempB.val if tempB else 0

            add = v1 + v2 + rem
            rem = add // 10

            temp.next = ListNode(add % 10)
            temp = temp.next

            if tempA:
                tempA = tempA.next
            if tempB:
                tempB = tempB.next
        return ans.next