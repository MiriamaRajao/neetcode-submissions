from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]):

        ROWS = len(grid)
        COLS = len(grid[0])

        queue = deque()

        elapsed = 0
        fresh = 0

        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        # Prefill rotten oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append([r,c])

                elif grid[r][c] == 1:
                    fresh += 1

        # Perform multi source BFS
        while queue and fresh > 0:

            for _ in range(len(queue)):
                r, c = queue.popleft()
                # Go through different directions
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                      continue

                    # Process only healthy cells
                    if grid[nr][nc] != 1:
                        continue

                    # Change to rotten
                    grid[nr][nc] = 2
                    queue.append([nr, nc])
                    fresh -= 1

            elapsed += 1

        return elapsed if fresh == 0 else -1



    

    




      

