class Solution:
    def solution_1049_5(self, n: int) -> str:
        n = list(str(n))
        current_count = 0
        
        # Idea is to loop in reverse and add a dot after every three digits
        for index in range(len(n) - 1, 0, -1):
            current_count += 1
            if current_count % 3 == 0:
                n.insert(index, '.')
        return (''.join(n))