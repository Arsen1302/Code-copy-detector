class Solution:
    def solution_413_4(self, nums: List[int]) -> int:
        
        frq = defaultdict(int) # frequency map for nums
        fnl = {} # stores first and last index of each num
        deg = 0  # degree
        
        for i in range(len(nums)):
            frq[nums[i]] += 1
            deg = max(deg, frq[nums[i]])
            if nums[i] in fnl:
                fnl[nums[i]][1] = i
            else:
                fnl[nums[i]] = [i,i]
                
        res = len(nums)
                
        for num in frq:
            if frq[num] != deg:
                continue
            res = min(res, fnl[num][1] - fnl[num][0] + 1)

        return res