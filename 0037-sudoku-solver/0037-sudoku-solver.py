class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        used_row = [set() for _ in range(9)]
        used_col = [set() for _ in range(9)]
        used_box = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    val = int(board[i][j])
                    used_row[i].add(val)
                    used_col[j].add(val)
                    box_id = (i // 3) * 3 + (j // 3)
                    used_box[box_id].add(val)

        def is_valid(i, j, val):
            box_id = (i // 3) * 3 + (j // 3)
            return val not in used_box[box_id] and val not in used_row[i] and val not in used_col[j]

        def dfs(i, j):
            if i == 9:
                return True
            next_i = next_j = 0
            if j < 8:
                next_i, next_j = i, j+1
            elif j == 8:
                next_i, next_j = i+1, 0
            if board[i][j] != ".":
                return dfs(next_i, next_j)

            box_id = (i // 3) * 3 + (j // 3)
            for x in range(1, 10):
                if is_valid(i, j, x):
                    board[i][j] = str(x)
                    used_row[i].add(x)
                    used_col[j].add(x)
                    used_box[box_id].add(x)
                    if dfs(next_i, next_j):
                        return True
                    board[i][j] = "."
                    used_row[i].remove(x)
                    used_col[j].remove(x)
                    used_box[box_id].remove(x)
            return False
        dfs(0, 0)
        return
