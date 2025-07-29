class Solution:
    def solution_98_3_1(self, numCourses: int, prerequisites):
        # DFS 用递归
        # 先找到 上了某门课以后可以解锁的全后置课，放入dict neighborNode 中
        # 再做一个 status dict, 用来记录查找的状态, 默认value 0 代表没访问过
        # solution_98_3_2 更改 status, 0 代表没访问; 1 代表访问中; 2 代表访问过
        # 如果递归遇到1，表示已成环，则无法上完所有课，返回 false；否则递归更新上课顺序在 result 里
        
        from collections import deque
        result=deque([])
        neighborNodes = collections.defaultdict(list)
        status = collections.defaultdict(int)
        
        for nodeTo,nodeFrom in prerequisites:
            neighborNodes[nodeFrom].append(nodeTo)
        
        def solution_98_3_2(node):
            if status[node]==1: 
                return False # 成环了，无法上完所有课
            if status[node]: 
                return #如果访问过了，退出
            
            status[node] = 1 #没访问过，递归，把顺序 appendleft 加入deque中
            for next_node in neighborNodes[node]:
                if solution_98_3_2(next_node) == False:
                    return False
            status[node] = 2
            result.appendleft(node)
            
        for node in range(numCourses):
            if solution_98_3_2(node) == False: 
                return []
        return result