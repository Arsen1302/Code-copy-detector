class Solution:
    def solution_1633_4(self, tasks: List[int], space: int) -> int:
        map = {tasks[0]:0}
        i = 1
        n = len(tasks)
        j = 1
        dash = 0
        while i<n:
            
            if tasks[i] in map and (i+dash)-map[tasks[i]] -1< space:
                count = space-((i+dash)-map[tasks[i]]-1)
                dash+=count
                j+= count
                map[tasks[i]] = i+dash
                i+=1
                j+=1
                
            else:
                map[tasks[i]] = i+dash
                j+=1
                i+=1
        return j