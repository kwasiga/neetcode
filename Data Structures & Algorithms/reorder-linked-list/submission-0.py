# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        # Get the middle and the end of the linked list 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Split the linked list at the half - slow = the middle
        second = slow.next
        prev = slow.next = None #Cut of the second half the linked list

        # Reverse Second Half on linked list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first, second = head, prev
        while second:
            x, y = first.next, second.next
            first.next = second
            second.next = x
            first, second = x, y


        
        