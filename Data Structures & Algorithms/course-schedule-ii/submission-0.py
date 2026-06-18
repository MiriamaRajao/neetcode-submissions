class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # Create adjacency list
        graph = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # Set to store the visiting, visited and order of courses
        visiting = set()
        visited = set()
        order = []

        # Define dfs
        def dfs(course):

            # If course is found in current visiting chain, return false
            if course in visiting:
                return False

            # If course is marked safe, add it to visited
            if course in visited:
                return True

            # Add current course to visiting
            visiting.add(course)

            # Check the prereq
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            # If all the prereq are there
            visiting.remove(course)
            visited.add(course)
            order.append(course)

            return True

        # Perform the dfs
        for course in range(numCourses):
            if not dfs(course):
                return []

        return order