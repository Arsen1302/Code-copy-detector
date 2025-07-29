class Solution:
    def solution_1266_3(self, memory1: int, memory2: int) -> List[int]:
        k = 1
        while k <= memory1 or k <= memory2: 
            if memory1 < memory2: memory2 -= k 
            else: memory1 -= k 
            k += 1
        return [k, memory1, memory2]