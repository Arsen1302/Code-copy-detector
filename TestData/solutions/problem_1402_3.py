class Solution:
    def solution_1402_3(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj_list = collections.defaultdict(list)
        indegree = [0] * n
        for prev, next in relations:
            adj_list[prev].append(next)
            indegree[next - 1] += 1

        queue = []

        for i in range(n):
            if not indegree[i]:
                heapq.heappush(queue, (time[i], i + 1))

        endtime = 0

        while queue:
            endtime, course = heapq.heappop(queue)

            for neighbor in adj_list[course]:
                indegree[neighbor - 1] -= 1
                if not indegree[neighbor - 1]:
                    heapq.heappush(queue, (endtime + time[neighbor - 1], neighbor))

        return endtime