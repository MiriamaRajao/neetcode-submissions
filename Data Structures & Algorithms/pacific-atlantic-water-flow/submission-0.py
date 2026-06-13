class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        prev_heights = 0

        # DFS from the outside of the ocean and getting inside

        def dfs(r, c, visited, prev_heights):
            # Check bounds
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return

            # Check if visited
            if (r, c) in visited:
                return

            # If an inaccessible box, then return
            if heights[r][c] < prev_heights:
                return

            # Add to visited
            visited.add((r, c))

            # Perform dfs to other nodes
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc, visited, heights[r][c])

            
        # Perform the dfs from the different sides of the rectangular triangle
        # Pacific
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])

        # Atlantic
        for r in range(ROWS):
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        for c in range(COLS):
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        # Check if the box is both in pacific and atlantic
        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append((r, c))


        return result

            




