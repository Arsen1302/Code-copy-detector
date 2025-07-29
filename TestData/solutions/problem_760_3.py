class Solution:
    def solution_760_3(self, dominoes: List[List[int]]) -> int:
        counter = defaultdict(int)
        for domino in dominoes: counter[tuple(sorted(domino))] +=1
        return sum([n*(n-1)//2 for n in counter.values()])