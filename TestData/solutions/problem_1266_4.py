class Solution:
    def solution_1266_4(self, memory1: int, memory2: int) -> List[int]:
        count = 0
        while memory1 or memory2:
            count +=1
            if memory1 >= memory2:
                if memory1-count >= 0:
                    memory1 -= count
                else:
                    return [count, memory1, memory2] 
            else:
                if memory2-count >= 0:
                    memory2 -= count
                else:
                    return [count, memory1, memory2] 
        return [1,0,0]