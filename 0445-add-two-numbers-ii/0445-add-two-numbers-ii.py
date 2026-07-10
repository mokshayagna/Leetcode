# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addition(self, head1, head2):
        head = head1
        c1 = head1
        c2 = head2
        carry = 0

        while c1:
            if c2:
                sum_val = c1.val + c2.val + carry
                c2 = c2.next
            else:
                sum_val = c1.val + carry

            c1.val = sum_val % 10
            carry = sum_val // 10

            if c1.next is None:
                if carry:
                    c1.next = ListNode(carry)
                    carry = 0
                break

            c1 = c1.next

        return head

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def length(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def addTwoNumbers(self, l1, l2):
        head1 = self.reverse(l1)
        head2 = self.reverse(l2)

        n = self.length(head1)
        m = self.length(head2)

        if n >= m:
            ans = self.addition(head1, head2)
        else:
            ans = self.addition(head2, head1)

        ans = self.reverse(ans)
        return ans