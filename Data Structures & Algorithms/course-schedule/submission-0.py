class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Create and fill adjacency list
        graph = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # Set for storing currently visiting chain and courses that have been visited
        visiting = set()
        visited = set()

        # DFS
        def dfs(course):

            # If course is in current visiting chain, cycle found, return false
            if course in visiting:
                return False

            # If course has already been added to visited, mark course as safe
            if course in visited:
                return True

            # Add current course into the visiting set
            visiting.add(course)

            # Perform a dfs on the prereq and return false if we found a cycle
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            # If cycle not found
            visiting.remove(course)
            visited.add(course)

            return True

        # Perform the dfs on all the courses
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

