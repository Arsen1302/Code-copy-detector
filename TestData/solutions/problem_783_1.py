class Solution:
    def solution_783_1(self, s: str, queries: List[List[int]]) -> List[bool]:
        prefix = [[0]*26]
        for c in s: 
            elem = prefix[-1].copy()
            elem[ord(c)-97] += 1
            prefix.append(elem)
        
        ans = []
        for left, right, k in queries: 
            cnt = sum(1&amp;(prefix[right+1][i] - prefix[left][i]) for i in range(26))
            ans.append(cnt <= 2*k+1)
        return ans