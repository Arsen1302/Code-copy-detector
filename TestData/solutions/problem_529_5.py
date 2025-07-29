class Solution:
    def solution_529_5(self, rooms: List[List[int]]) -> bool:
        seen = [False]*len(rooms)
        stack = [0]
        while stack: 
            n = stack.pop()
            if not seen[n]:
                seen[n] = True 
                stack.extend(rooms[n])
        return all(seen)