class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)
                else:
                    empty_cells.append((r, c))

        def backtrack(index):
            if index == len(empty_cells):
                return True
            
            r, c = empty_cells[index]
            box_idx = (r // 3) * 3 + (c // 3)
            
            for i in range(1, 10):
                st = str(i)
                if st not in rows[r] and st not in cols[c] and st not in boxes[box_idx]:
                    board[r][c] = st
                    rows[r].add(st)
                    cols[c].add(st)
                    boxes[box_idx].add(st)
                    
                    if backtrack(index + 1):
                        return True
                    
                    board[r][c] = "."
                    rows[r].remove(st)
                    cols[c].remove(st)
                    boxes[box_idx].remove(st)
            return False

        backtrack(0)                                                    


        