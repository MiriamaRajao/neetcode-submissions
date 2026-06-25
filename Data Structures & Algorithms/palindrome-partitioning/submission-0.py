from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        def backtrack(start):
            # If we used the whole string, save this partition
            if start == len(s):
                result.append(path.copy())
                return

            # Try every possible ending point from this start
            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    piece = s[start:end + 1]

                    # Choose
                    path.append(piece)

                    # Explore rest
                    backtrack(end + 1)

                    # Undo
                    path.pop()

        backtrack(0)
        return result