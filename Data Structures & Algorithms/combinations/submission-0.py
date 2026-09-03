class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def combinations(cur_n, cur_comb, k, n):
            
            if len(cur_comb) == k:
                answer.append(cur_comb)
                return 
            
            if cur_n > n:
                return 
            

            combinations(cur_n + 1, cur_comb, k, n)
            combinations(cur_n + 1, cur_comb + [cur_n], k, n)
            
        combinations(1, [], k, n)
        return answer