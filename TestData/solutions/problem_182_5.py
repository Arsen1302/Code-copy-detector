class Solution:
    def solution_182_5(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        total = jug1Capacity+jug2Capacity
        visit = set()
        visit.add(0)
        q = [0]
        while q:
            curr = q.pop(0)
            if curr == targetCapacity:
                return True
            for step in [jug1Capacity, -jug1Capacity, jug2Capacity, -jug2Capacity]:
                new = curr+step
                if new > 0 and new <= jug1Capacity+jug2Capacity and new not in visit:
                    visit.add(new)
                    q.append(new)
        return False