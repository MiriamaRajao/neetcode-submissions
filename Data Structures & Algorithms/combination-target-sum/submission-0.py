class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        # Definition of the backtracking solution
        def backtrack(i, total):
            # Case if we have the target number
            if total == target:
                result.append(path.copy())
                return

            # If we exceed total or reach the end of i, then also return
            if total > target or i == len(nums):
                return

            # Make the 2 choices: to include current nums[i] or to skip
            # Choice 1: include
            path.append(nums[i])
            backtrack(i, total + nums[i])

            # Undo choice
            path.pop()

            # Choice 2: ignore current val and immediately go to next
            backtrack(i + 1, total)

        # Call backtrack
        total = 0
        backtrack(0, total)

        # Return result
        return result