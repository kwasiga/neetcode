# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [0, 1, 2, 3] -> [0, 1] - [2, 3]
# [0, 3, 1, 2]

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        h2 = slow.next
        prev = slow.next = None

        while h2:
            temp = h2.next
            h2.next = prev
            prev = h2
            h2 = temp

        h1, h2 = head, prev
        while h2:
            x, y = h1.next, h2.next
            h1.next = h2
            h2.next = x
            h1, h2 = x, y

            
                



            


        