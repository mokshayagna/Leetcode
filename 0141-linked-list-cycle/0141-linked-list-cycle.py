# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        h = {}
        temp = head
        if head is None:
            return False
        if head.next is None:
            return False
        while temp is not None:
            if temp.next not in h:
                h[temp.next] = 1
                temp = temp.next
            else:
                return True
        return False