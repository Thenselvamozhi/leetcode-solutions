# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        temp = ans
        tempA, tempB = list1, list2
        while tempA and tempB:
            if tempA.val < tempB.val:
                temp.next = tempA
                tempA = tempA.next
                temp = temp.next
            else:
                temp.next = tempB
                tempB = tempB.next
                temp = temp.next
        if tempA:
            temp.next = tempA
        if tempB:
            temp.next = tempB
        return ans.next