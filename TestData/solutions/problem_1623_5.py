class Solution:
    def solution_1623_5(self, rolls: List[int], k: int) -> int:
        res = 0
        s = set()
        for i in range(len(rolls)):
            num = rolls[i]
            if num not in s:
                s.add(num)
                if len(s) == k:
                    res+=1
                    s = set()
        return res+1