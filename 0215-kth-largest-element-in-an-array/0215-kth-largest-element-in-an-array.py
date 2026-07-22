from typing import List

class Solution:

    def min_heapify(self, a, i):
        while True:
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(a) and a[left] < a[smallest]:
                smallest = left

            if right < len(a) and a[right] < a[smallest]:
                smallest = right

            if smallest == i:
                break

            a[i], a[smallest] = a[smallest], a[i]
            i = smallest

    def min_heap(self, a):
        n = len(a)
        for i in range(n // 2 - 1, -1, -1):
            self.min_heapify(a, i)

    def kth(self, a, nums):
        # Start from k because first k elements are already in the heap
        for i in range(len(a), len(nums)):
            if nums[i] > a[0]:
                a[0] = nums[i]
                self.min_heapify(a, 0)

        return a[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        a = nums[:k]         
        self.min_heap(a)
        return self.kth(a, nums)