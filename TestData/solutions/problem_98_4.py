class Solution:
    def solution_98_4(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # BFS 用deque
        from collections import deque
        q = deque([])
        result = deque([])
        inDegree = [0]*numCourses
        neighborNodes = collections.defaultdict(list)
        
        # 计算每一门课的入度, 找到 每一门 course 可以解锁的课程
        for nodeTo, nodeFrom in prerequisites:
            inDegree[nodeTo] +=1
            neighborNodes[nodeFrom].append(nodeTo)
        
        # 将入度=0 的课程放入 deque 中，可以先上
        for node in range(numCourses):
            if not inDegree[node]:
                q.append(node)
                
                
        while q:
            node = q.pop()
            result.append(node)
            for next_node in neighborNodes[node]:
                inDegree[next_node] -=1
                if not inDegree[next_node]: q.append(next_node)
        
        # 如果有环，则 上过课的数量会小于 课程总数，返回[]
        if len(result) == numCourses: return result
        return []