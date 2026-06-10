from collections import deque
import math

class Solution:
	def islandsAndTreasure(self, grid: List[List[int]]) -> None:
		# Use multi source BFS
		ROWS = len(grid)
		COLS = len(grid[0])
		INF = 2147483647
		
		queue = deque()
		
		directions = [
			(1, 0),
			(-1, 0),
			(0, 1),
			(0, -1)
		]
		
		# Fill deque with all the treasure islands at 0, and start the analysis there
		for r in range(ROWS):
			for c in range(COLS):
				if grid[r][c] == 0:
					queue.append((r, c))
					
		# Loop through the deque
		
		while queue:
			# Process queue
			r, c = queue.popleft()
			
			# Loop through possible directions
			for dr, dc in directions:
				nr = r + dr
				nc = c + dc
				
				# Check bounds
				if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
					continue
					
				# Modify blocks that are inf to be their distance from the treasure island
				if grid[nr][nc] == INF:
					grid[nr][nc] = grid[r][c] + 1
					# Add it to the queue
					queue.append((nr, nc)) 