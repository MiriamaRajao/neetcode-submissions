class Solution:
	def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
		# Edge case
		if not grid:
			return 0

		rows, cols = len(grid), len(grid[0])
		directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
		max_land_area = 0

		# dfs helper function to traverse the graph and return the area of the current island being processed
		def dfs(i, j):
			# Return if i and j are out of bonds, if grid[i][j] == "0" or if (i, j) already visited
			if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0 or (i, j) in visited:
				return 0

			# Mark node as visited
			visited.add((i, j))

			# Add to area
			area = 1

			# DFS through neighbors
			for dx, dy in directions:
				new_x, new_y = i + dx, j + dy
				area += dfs(new_x, new_y)

			return area

		# Loop through the grid
		visited = set()

		for i in range(rows):
			for j in range(cols):
				if grid[i][j] == 1 and (i, j) not in visited:
					max_land_area = max(max_land_area, dfs(i, j))

		# Return function
		return max_land_area

# T C : O(m x n)
# S C : O(m x n)