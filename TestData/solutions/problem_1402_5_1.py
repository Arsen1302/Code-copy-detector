class Solution:
    def solution_1402_5_1(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = collections.defaultdict(list)
        prv_set = set()
        for prv, nxt in relations:
            graph[nxt-1].append(prv-1)
            prv_set.add(prv-1)
        
        course_not_prv = list(set(range(0,n))-prv_set)

        @lru_cache(None)
        def solution_1402_5_2(course):
            prevs = graph[course]
            cost = 0
            for p in prevs:
                cost = max(cost, solution_1402_5_2(p))
            return cost + time[course]


        return max(solution_1402_5_2(course) for course in course_not_prv)