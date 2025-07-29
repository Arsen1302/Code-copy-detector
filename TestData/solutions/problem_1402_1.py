class Solution:
    def solution_1402_1(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = { course:[] for course in range(n)}
        inDegree = [0]*n
        # 1- build graph
        #  convert 1-base into 0-baseindexes and add to graph
        # Note: choose Prev->next since it helps to preserve the topology order
        for prevCourse,nextCourse in relations:
            prevCourse,nextCourse = prevCourse-1, nextCourse-1
            graph[prevCourse].append(nextCourse)
            inDegree[nextCourse] += 1

        # 2 Assign time cost
        q = collections.deque()
        cost = [0] * n
        for course in range(n):
            if inDegree[course] == 0:
                q.append(course)
                cost[course] = time[course] # number of months
        # 3- BFS
        while q:
            prevCourse = q.popleft()
            for nextCourse in graph[prevCourse]:
                # Update cost[nextCourse] using the maximum cost of the predecessor course
                cost[nextCourse] = max(cost[nextCourse], cost[prevCourse] + time[nextCourse])
                inDegree[nextCourse] -= 1
                if inDegree[nextCourse] == 0:
                    q.append(nextCourse)
        return max(cost)
		```