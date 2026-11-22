class TimeMap:

    def __init__(self):
        from collections import defaultdict
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        cur_list = self.storage[key]
        
        left, right = 0, len(cur_list) - 1
        if not cur_list or cur_list[left][0] > timestamp:
            return ""
        # print(right, cur_list)
        if cur_list[right][0] <= timestamp:
            return cur_list[right][1]

        while left + 1 < right:
            mid = (left + right) // 2
            if cur_list[mid][0] <= timestamp:
                left = mid
            else:
                right = mid

        return cur_list[left][1]