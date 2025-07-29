class Solution:
    def solution_96_2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = { courseNum : [] for courseNum in range(numCourses) }
        
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
         
        Course = namedtuple('Course', ['number', 'backtrack'])
        
        for courseNum in range(numCourses):
            
            currCourse = Course(courseNum, False)
            
            stack = [currCourse]            
            visited = set([currCourse.number])
            
            while stack:
                currCourse = stack.pop()
                
                if currCourse.backtrack:
                    graph[currCourse.number] = []
                    visited.discard(currCourse.number)                    
                    continue
                
                stack.append(Course(currCourse.number, True))
                visited.add(currCourse.number)
                
                for prereqCourseNum in graph[currCourse.number]:
                    if prereqCourseNum in visited:
                        return False
                    
                    stack.append(Course(prereqCourseNum, False))
                    
        return True