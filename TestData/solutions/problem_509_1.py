class Solution:
    def solution_509_1(self, s: str, c: str) -> List[int]:
        L = []
        for idx, value in enumerate(s):
            if value == c:
                L.append(idx)
        
        distance = []
        i = 0
        for idx, value in enumerate(s):
            if value == c:
                distance.append(0)
                i += 1
            elif idx < L[0]:
                distance.append(L[0] - idx)
            elif idx > L[-1]:
                distance.append(idx - L[-1])
            else:
                distance.append(min((L[i] - idx), (idx - L[i-1])))                    
        return distance