class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        # Perform backtracking for each index
        def backtrack(i):
            # If we have reached last index, get the result and return
            if i == len(nums):
                result.append(path.copy())
                return

            # Make 2 choices: include current nums[i] or ignore
            path.append(nums[i])
            backtrack(i + 1)

            # Undo choice
            path.pop()

            # Choice 2: do not include current num
            backtrack(i + 1)

        # Call the backtracking code
        backtrack(0)

        return result
        