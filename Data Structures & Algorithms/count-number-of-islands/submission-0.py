class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		# Edge cases
		if not grid:
			return 0

		rows, cols = len(grid), len(grid[0])
		directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

		# Number of islands
		number_islands = 0

		# dfs helper function
		def dfs(i, j):
			# Return when i and j are out of range or if grid[i][j] == 0
			if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == "0" or (i, j) in visited:
				return

			# Mark node as visited
			visited.add((i, j))

			# Process neighboring nodes
			for dx, dy in directions:
				new_x, new_y = i + dx, j + dy
				dfs(new_x, new_y)
				

		# loop through the different grid and do a dfs to mark neigboring 1
		visited = set()

		for i in range(rows):
			for j in range(cols):
				if grid[i][j] == "1" and (i, j) not in visited:
					number_islands += 1
					dfs(i, j)

		# Return
		return number_islands

# T C : O(m x n) for m is rows and n is columns
# S C : O(m x n) recursion stack and visited set