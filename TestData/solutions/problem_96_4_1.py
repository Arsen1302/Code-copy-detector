class Solution:
    def solution_96_4_1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseGraph = [[] for _ in range(numCourses)]
        for ai, bi in prerequisites:
            courseGraph[ai].append(bi)

        visited = [False] * numCourses
        stack = defaultdict(bool)
        for c in range(numCourses):
            if not self.solution_96_4_2(c, courseGraph, visited, stack):
                return False
        return True
    
    def solution_96_4_2(self, c, courseGraph, visited, stack):

        if stack[c]:            # if present in running stack, it's a cycle
            return False
        stack[c] = True         # add to running stack
        for prereq in courseGraph[c]:
            if visited[prereq] == True:    # if this pre-req is already visited True, then it was fully processed in the past and no cycle going down this path, so we can skip now.
                continue
            if not self.solution_96_4_2(prereq, courseGraph, visited, stack):
                return False
        stack[c] = False        # remove from running stack
        visited[c] = True       # mark it visited True when it is fully processed
        return True