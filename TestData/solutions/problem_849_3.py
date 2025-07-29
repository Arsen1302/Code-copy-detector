class Solution:
    def solution_849_3(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n%k != 0:
            return False
        
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        while d:
            mn = min(d.keys())
            for i in range(k):
                if (mn+i) in d:
                    if d[(mn+i)] == 1:
                        del d[(mn+i)]
                    else:
                        d[(mn+i)] -= 1
                else:
                    return False
        
        return True