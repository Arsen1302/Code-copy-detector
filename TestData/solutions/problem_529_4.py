class Solution:
#     Runtime: 96ms 48.98% memory: 14.4mb 85.04%
    def solution_529_4(self, rooms: List[List[int]]) -> bool:
        seen = set()
        stack = [0]
        seen.add(stack[-1])
        
        while stack:
            cur = stack.pop()
            for neigh in rooms[cur]:
                if not neigh in seen:
                    seen.add(neigh)
                    stack.append(neigh)
                    
        
        return len(seen) == len(rooms)