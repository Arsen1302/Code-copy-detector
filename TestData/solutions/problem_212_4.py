class Solution:
    def solution_212_4(self, num: int) -> List[str]:
        if num < 0 or num > 10:
            return []
        
        result = []
        
        for hour in range(0, 12):
            for minute in range(0, 60):
                if bin(hour).count('1') + bin(minute).count('1') == num:
                    result.append('{:d}:{:02d}'.format(hour, minute))
                    
        return result