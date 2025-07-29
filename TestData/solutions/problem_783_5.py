class Solution:
    def solution_783_5(self, s: str, queries: List[List[int]]) -> List[bool]:
        runningCount = [[0]*26]
        countSnapshot = [0]*26
        a = ord("a")
        for c in s:
            countSnapshot[ord(c)-a] += 1
            runningCount.append([*countSnapshot]) # the * is necessary to deep copy the list
        
        for left,right,k in queries:
            if k>=13:
                yield True
                continue
            odds = 0
            for i in range(26):
                odds += (runningCount[right+1][i] - runningCount[left][i])%2
            yield k>=odds//2