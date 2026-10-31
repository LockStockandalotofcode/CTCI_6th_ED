class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        used_row = [set() for _ in range(9)]
        used_col = [set() for _ in range(9)]
        used_box = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    val = int(board[r][c])
                    used_row[r].add(val)
                    used_col[c].add(val)
                    box_id = (r // 3) * 3 + (c // 3)
                    used_box[box_id].add(val)

        def is_valid(r, c, val):
            box_id = (r // 3) * 3 + (c // 3)
            return val not in used_box[box_id] and val not in used_row[r] and val not in used_col[c]

        def dfs(r, c):
            if r == 9:
                return True
            next_r = next_c = 0
            if c < 8:
                next_r, next_c = r, c+1
            elif c == 8:
                next_r, next_c = r+1, 0
            if board[r][c] != ".":
                return dfs(next_r, next_c)

            box_id = (r // 3) * 3 + (c // 3)
            for val in range(1, 10):
                if is_valid(r, c, val):
                    # update the board
                    board[r][c] = str(val)
                    used_row[r].add(val)
                    used_col[c].add(val)
                    used_box[box_id].add(val)
                    # recurse
                    if dfs(next_r, next_c):
                        return True
                    # backtrack, if it didnt work
                    board[r][c] = "."
                    used_row[r].remove(val)
                    used_col[c].remove(val)
                    used_box[box_id].remove(val)
            return False
        dfs(0, 0)
        return
