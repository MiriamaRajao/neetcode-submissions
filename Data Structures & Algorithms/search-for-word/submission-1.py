class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS = len(board)
        COLS = len(board[0])

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        visited = set()

        # Perform DFS
        def dfs(i, j, idx):
            # If current idx is equal to word length we found our word
            if idx == len(word):
                return True

            # If out of bounds, return false
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return False

            # If visited, also return as false
            if (i, j) in visited:
                return False
        
            # If current word do not match the word idx, return false
            if board[i][j] != word[idx]:
                return False

            # Otherwise process this node and mark it as visited
            visited.add((i, j))

            # Do a DFS on neighbors
            for dr, dc in directions:
                next_i = i + dr
                next_j = j + dc
                if dfs(next_i, next_j, idx + 1):
                    return True

            # Undo choice
            visited.remove((i, j))

            return False

        # Call dfs
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True

        return False