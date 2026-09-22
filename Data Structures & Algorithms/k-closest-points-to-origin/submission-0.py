class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq

        heap = []

        for point in points:
            x, y = point
            dist = x**2 + y**2

            heapq.heappush(heap, (-dist, point))
            if len(heap) > k:
                heapq.heappop(heap)
            
        return [elem[1] for elem in heap]