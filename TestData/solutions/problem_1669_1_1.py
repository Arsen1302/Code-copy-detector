class Solution:
    def solution_1669_1_1(self, nums: List[int]) -> List[int]:

        def solution_1669_1_2(m):
            t = 0
            for n in m:
                if m[n] > 0:
                    t = t | (1 << n)
            return t
        
        def solution_1669_1_3(a,m):
            ans = bin( a )
            s = str(ans)[2:]
            for i, b in enumerate( s[::-1]):
                if b == '1':
                    m[i] += 1

        def solution_1669_1_4(a,m):
            ans = bin( a )
            s = str(ans)[2:]
            for i, b in enumerate( s[::-1]):
                if b == '1':
                    m[i] -= 1
        
        res = []

        
        n = defaultdict(int)
        for i in nums:
            solution_1669_1_3(i,n)

        
        m = defaultdict(int)
        r = 0
        c = 0

        for i,v in enumerate(nums):
            # The last check is for if nums[i] == 0, in that case we still want to solution_1669_1_3 to the map
            while r < len(nums) and (solution_1669_1_2(m) != solution_1669_1_2(n) or (c==0 and nums[i] ==0)):
                solution_1669_1_3(nums[r],m)
                r+=1
                c+=1

            res.append(c)

            solution_1669_1_4(nums[i],m)
            solution_1669_1_4(nums[i],n)
            c-=1

        return res