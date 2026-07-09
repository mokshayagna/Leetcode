class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        count = 0

        while temp is not None:
            count += 1
            temp = temp.next

        mid = count // 2

        temp = head
        for _ in range(mid):
            temp = temp.next

        return temp