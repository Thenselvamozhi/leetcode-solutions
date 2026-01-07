# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Brute force approach is where you create a stack and add all the elements from the list and append themfrom the end into a new ll
        st = []
        temp = head
        while temp:
            st.append(temp)
            temp = temp.next
        head = ListNode()
        temp1 = head
        while temp1:
            temp1 = st.pop()'''
        
        #Optimal approach
        curr = head
        prev = None
        while curr:
           front = curr.next
           curr.next = prev
           prev = curr
           curr = front
        return prev