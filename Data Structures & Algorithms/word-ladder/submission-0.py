from collections import deque, defaultdict
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # If endWord is not in wordList, just return 0
        if endWord not in wordList:
            return 0

        # Length of the word
        len_word = len(beginWord)

        # Fill out a lookout dict to find all possible path from a starting word
        lookout_dict = defaultdict(list)

        for word in wordList:
            for i in range(len_word):
                current_tag = word[:i] + '*' + word[i+1:]
                lookout_dict[current_tag].append(word)

        # Start BFS where we have a deque with the length of the current BFS level
        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        # BFS
        while queue:
            # Pop current word
            current_word, length = queue.popleft()

            # Check the appropriate word we should try next
            for i in range(len_word):
                current_tag = current_word[:i] + '*' + current_word[i+1:]

                # Look at all possibilities for this tag
                for neighbor in lookout_dict[current_tag]:
                    # Check if we have reached endWord
                    if neighbor == endWord:
                        return length + 1

                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, length + 1))

        # Otherwise, we didn't find any valid path
        return 0

        

            
