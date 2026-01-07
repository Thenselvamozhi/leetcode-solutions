# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def length(self, head):
        l = 0
        temp = head
        while temp:
            l += 1
            temp = temp.next
        return l
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1 = self.length(headA)
        l2 = self.length(headB)

        diff = l1 - l2

        if diff > 0:
            tempA = headA
            while diff > 0:
                tempA = tempA.next
                diff -= 1
            tempB = headB
            while tempA and tempB and tempA != tempB:
                tempA = tempA.next
                tempB = tempB.next
            return tempA

        else:
            tempB = headB
            while diff < 0:
                tempB = tempB.next
                diff += 1
            tempA = headA
            while tempA and tempB and tempA != tempB:
                tempA = tempA.next
                tempB = tempB.next
            return tempA
        return None