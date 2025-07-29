class Solution:
    def solution_212_5_1(self, turnedOn: int) -> List[str]:
        # for example:
        # 2 1 (3 min) - two leds on, bin: 11 
        # 2   (2 min) - one led on, bin: 10
        #   1 (1 min) - one led on, bin:  1
        
        def solution_212_5_2(n):
            s = bin(n)[2:]
            temp = 0
            for i in s:
                if i == '1':
                    temp += 1
            return temp
        
        result = []
        
        for h in range(12):
            for m in range(60):
                if solution_212_5_2(h) + solution_212_5_2(m) == turnedOn:
                    result.append(f'{h}:{m:02}')
                    
        return result