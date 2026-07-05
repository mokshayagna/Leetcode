# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        temp = head
        while temp is not None:
            l.append(str(temp.val))
            temp = temp.next
        s = "".join(l)
        return s == s[::-1]