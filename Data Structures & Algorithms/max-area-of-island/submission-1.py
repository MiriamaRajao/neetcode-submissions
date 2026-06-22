class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Geometry
        ROWS = len(grid)
        COLS = len(grid[0])

        # Directions
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        # Visited set
        visited = set()

        # Max area
        max_area = 0

        # Deifinition of DFS to explore the grid
        def dfs(i, j):
            # Area var
            nonlocal area

            # Check if we are out of bounds
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return

            # Check if we hit a water, if so then return
            if grid[i][j] == 0:
                return

            # If we have already visite this cell, return
            if (i, j) in visited:
                return

            # Otherwise process node and add it in visited
            visited.add((i, j))

            # Add to area
            area += 1

            # Go though neighboring celss
            for dr, dc in directions:
                next_i = i + dr
                next_j = j + dc
                dfs(next_i, next_j)

        # Explore the grid
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visited and grid[i][j] == 1:
                    # Start a new area
                    area = 0
                    dfs(i, j)
                    max_area = max(max_area, area)

        # Return max_area
        return max_area
