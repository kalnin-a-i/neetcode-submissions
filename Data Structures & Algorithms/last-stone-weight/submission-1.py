class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        heap = [(-stones[i], stones[i]) for i in range(len(stones))]
        heapq.heapify(heap)
        # print(heap)
        while len(heap) > 1:
            # print(heap)
            x = heapq.heappop(heap)[1]
            y = heapq.heappop(heap)[1]

            if x == y:
                continue
            else:
                heapq.heappush(heap, (-abs(x-y), abs(x-y)))
        print(heap)
        if not heap:
            return 0
        return heap[0][1]