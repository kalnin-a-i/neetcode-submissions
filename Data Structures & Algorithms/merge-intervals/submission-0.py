class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        cur_interval = intervals[0]
        answer = []
        for interval in intervals:
            if interval[0] <= cur_interval[1]:
                cur_interval[1] = max(cur_interval[1], interval[1])
            else:
                answer.append(cur_interval)
                cur_interval = interval

        answer.append(cur_interval)
        return answer