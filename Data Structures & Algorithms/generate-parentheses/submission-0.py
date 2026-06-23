class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []

        # Define backtrack function which keeps track of open and closed counts
        def backtrack(open_count, closed_count):
            # If we have arrived at count = 2 * n, then we record path
            if len(path) == 2 * n:
                result.append("".join(path))
                return

            # Make 2 choices: add ( or )
            # Choice 1: Opening
            if open_count < n:
                path.append("(")
                backtrack(open_count + 1, closed_count)
                # Undo choice
                path.pop()

            # Choice 2: Closing
            if closed_count < open_count:
                path.append(")")
                backtrack(open_count, closed_count + 1)
                # Undo choice
                path.pop()

        # Call backtrack
        backtrack(0, 0)

        return result