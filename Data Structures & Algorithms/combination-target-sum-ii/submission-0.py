class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort candidates to facilitate not reusing duplicate combinations
        candidates.sort()

        result = []
        path = []

        # Backtracking solution
        def backtrack(i, total):
            # If we have the target, append to result
            if total == target:
                result.append(path.copy())
                return

            # IF we also overshoot total or at the end of the list, return
            if total > target or i == len(candidates):
                return

            # Make 2 choices, accept current nums[i] and then immediately move to the next idx (as it cannot be reused)
            path.append(candidates[i])
            backtrack(i + 1, total + candidates[i])

            # Undo choice
            path.pop()

            # Choice 2, skip values, but also skip all values with the same idx?
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, total)

        # Call backtrack
        total = 0
        backtrack(0, total)

        return result