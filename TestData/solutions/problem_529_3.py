class Solution:
    def solution_529_3(self, rooms: List[List[int]]) -> bool:

        n = len(rooms)
        seen = [False] * n
        stack = [0]  # room 0 is unlocked
        while stack:
            room = stack.pop()
            if not seen[room]:  # if not previously visited
                seen[room] = True
                for key in rooms[room]:
                        stack.append(key)
        
        return all(seen)