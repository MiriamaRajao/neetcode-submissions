class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS = len(board)
        COLS = len(board[0])

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        visited = set()

        def dfs(r, c, visited):

            # Check if out of bonds
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return

            # Check if in visited
            if (r, c) in visited:
                return

            # Add to visited
            visited.add((r, c))

            # Check if it is still an O, mark as safe, otherwise return
            if board[r][c] == 'O':
                # Mark as safe
                board[r][c] = 'S'
            else:
                return

            # Do a dfs for the different directions
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc, visited)

        # Perform the dfs from all the 0s in the edge
        for r in range(ROWS):
            dfs(r, 0, visited)
            dfs(r, COLS - 1, visited)

        for c in range(COLS):
            dfs(0, c, visited)
            dfs(ROWS - 1, c, visited)


        # Change the S which are safe as 0s, and other 0s as X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'
