# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        h = {}
        temp = head
        while temp is not None:
            if temp.next in h:
                return True
            h[temp] = 1
            temp = temp.next
        return False