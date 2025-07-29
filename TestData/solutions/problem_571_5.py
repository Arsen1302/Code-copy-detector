class Solution:
    def solution_571_5(self, A: str, B: str) -> List[str]:
        unique = []
        sentences = A.split(" ") + B.split(" ")
        
        for i in sentences:
            if sentences.count(i) == 1:
                unique.append(i)
        return unique