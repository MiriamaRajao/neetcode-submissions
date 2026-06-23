class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort nums to facilitate removing duplicates
        nums.sort()

        result = []
        path = []

        # Backtracking function to form the subset
        def backtrack(i):
            # If we have reached the end, return
            if i == len(nums):
                result.append(path.copy())
                return

            # Make 2 choices, to add or to skip
            # Choice 1: keep
            path.append(nums[i])
            backtrack(i + 1)

            # Undo choice
            path.pop()

            # Choice 2: skip this value, but then also skip other similar values
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

        # Start backtrack from starting index
        backtrack(0)
        return result
        