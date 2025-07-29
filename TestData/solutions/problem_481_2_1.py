class Solution:
    def solution_481_2_1(self, order: str, s: str) -> str:
        
        def solution_481_2_2(x):
            return rank[ord(x) - ord('a')]
        
        rank = [26]*26
        
        for i in range(len(order)):
            rank[ord(order[i]) - ord('a')] = i
        
        
        print(rank)
        arr = [i for i in s]
        
        arr.sort(key= solution_481_2_2)
        
        s = "".join(arr)
        
        return s