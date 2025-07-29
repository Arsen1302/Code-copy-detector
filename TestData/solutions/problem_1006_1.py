class Solution:
    def solution_1006_1(self, arr: List[int], k: int) -> bool:
        freq = dict()
        for x in arr: freq[x%k] = 1 + freq.get(x%k, 0)
        return all(freq[x] == freq.get(xx:=(k-x)%k, 0) and (x != xx or freq[x]%2 == 0) for x in freq)