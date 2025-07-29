class Solution:
def solution_217_3(self, people: List[List[int]]) -> List[List[int]]:
    people.sort(key = lambda x: (-x[0], x[1]))
    queue = []
    for p in people:
        queue.insert(p[1], p)   
    return queue