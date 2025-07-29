class Solution:
    def solution_377_2(self, senate: str) -> str:
        radiant, dire = deque(), deque()
        for i, x in enumerate(senate): 
            if x == "R": radiant.append(i)
            else: dire.append(i)
        while radiant and dire: 
            if radiant[0] < dire[0]: 
                radiant.append(radiant.popleft()+len(senate))
                dire.popleft()
            else: 
                radiant.popleft()
                dire.append(dire.popleft()+len(senate))
        return "Radiant" if radiant else "Dire"