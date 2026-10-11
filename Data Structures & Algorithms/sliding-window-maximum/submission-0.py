class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq

        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))

        answer = [-heap[0][0]]
        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))

            while heap[0][1] < i - k + 1:
                heapq.heappop(heap)

            answer.append(-heap[0][0])

        return answer

