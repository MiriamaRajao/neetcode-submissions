from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = set()

        # Definition of the backtracking
        def backtrack():
            # If path length is equal to len(nums), we have a valid answer so we return
            if len(path) == len(nums):
                result.append(path.copy())
                return

            # Then explore all possible numbers
            for num in nums:
                # If it hase been used, then we continue
                if num in used:
                    continue

                # Otherwise, choose num and mark it as used
                path.append(num)
                used.add(num)

                # Explore other possibilities from here
                backtrack()

                # Then undo that choice
                path.pop()
                used.remove(num)

        backtrack()

        return result