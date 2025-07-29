class Solution:
    def solution_1266_5(self, memory1: int, memory2: int) -> List[int]:
        for sec in range(1, memory1 + memory2 + 2):
            if memory1 >= memory2:
                if sec <= memory1:
                    memory1 -= sec
                else:
                    return [sec, memory1, memory2]
            else:
                if sec <= memory2:
                    memory2 -= sec
                else:
                    return [sec, memory1, memory2]