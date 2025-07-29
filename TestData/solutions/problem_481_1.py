class Solution:
    def solution_481_1(self, order: str, s: str) -> str:

        rank = [26]*26
        
        for i in range(len(order)):
            rank[ord(order[i]) - ord('a')] = i

        return "".join(sorted(list(s), key= lambda x: rank[ord(x) - ord('a')]))