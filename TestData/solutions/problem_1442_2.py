class Solution:
    def solution_1442_2(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        a, b = 0, len(plants) - 1
        waterA, waterB = capacityA, capacityB
        res = 0
        while a < b:
            if waterA < plants[a]:
                res += 1
                waterA = capacityA
            waterA -= plants[a]
            a += 1
            
            if waterB < plants[b]:
                res += 1
                waterB = capacityB
            waterB -= plants[b]
            b -= 1
        
        if a == b and waterA < plants[a] and waterB < plants[a]:
            res += 1
        return res