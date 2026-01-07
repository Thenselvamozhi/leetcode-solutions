# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #s1 -> Find the middle
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        #s2 -> break from the middle
        second_head = slow.next
        slow.next = None
        prev = None
        curr = second_head
        #s3 -> Reverse the second part of the list
        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        tempA = head
        tempB = prev
        while tempB and tempA:
            if tempA.val != tempB.val:
                return False
            tempA = tempA.next
            tempB = tempB.next

        return True
                