class Solution:
    def solution_618_5(self, logs: List[str]) -> List[str]:
        digit = []
        letter = []
        
        for log in logs:
            if log[-1].isdigit():
                digit.append(log)
            else:
                letter.append(log)
                
        letter = [x.split(" ", maxsplit=1) for x in letter]
    
        letter = sorted(letter, key = lambda x: (x[1], x[0]))
        
        letter = [' '.join(map(str, x)) for x in letter]
        
        return letter + digit