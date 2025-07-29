class Solution:
    def solution_96_3(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Data Structures and Variables
        in_degree = [0] * numCourses
        adj_list = [[] for x in range(numCourses)]
        queue = []
        counter = 0
        
        #building in_degree list and adj_list
        for course, prereq in prerequisites:
            in_degree[course] += 1
            adj_list[prereq].append(course)
            
        #enqueing nodes with no dependencies
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
                
        #Khans Algorithm
        #Remove Nodes without dependencies and decrement the in-degrees of the nodes
        #in their adj_list
        while(queue != []):
            node = queue.pop(0)
            counter += 1
            for dependent in adj_list[node]:
                in_degree[dependent] += -1
                if in_degree[dependent] == 0:
                    queue.append(dependent)
        #check for cycle
        if counter != numCourses:
            return False
        
        return True