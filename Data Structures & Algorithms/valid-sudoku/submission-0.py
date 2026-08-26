from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_rows = defaultdict(set)
        seen_cols = defaultdict(set)
        seen_sq = defaultdict(set)
        n, m = len(board), len(board[0])

        def get_sq_number(i, j):
            row = i // 3
            col = j // 3
            return 3 * row + col

        for i in range(n):
            for j in range(m):
                sq_num = get_sq_number(i, j)
                if board[i][j] != ".":
                    if board[i][j] in seen_cols[j] or board[i][j] in seen_rows[i] or board[i][j] in seen_sq[sq_num]:
                        return False
                    seen_rows[i].add(board[i][j])
                    seen_cols[j].add(board[i][j])
                    seen_sq[sq_num].add(board[i][j])
        
        return True