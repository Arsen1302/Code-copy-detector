class Solution:
    def solution_1134_1(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        
        count = 0
        for x in nums:
            comp = k - x
            if counter[comp]>0:
                counter[comp]-=1
                count+=1
            else:
                counter[x] +=1
        
        return count