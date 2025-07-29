class Solution:
    
    def solution_529_2_1(self,rooms,index,visited):
        if index not in visited:
            visited.add(index)
            for i in rooms[index]:
                self.solution_529_2_1(rooms,i,visited)
    
    def solution_529_2_2(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self.solution_529_2_1(rooms,0,visited)
        return len(visited)==len(rooms)