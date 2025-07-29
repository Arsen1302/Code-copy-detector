class Solution:
    def solution_676_5_1(self,num):
        return int(num**0.5)**2 == num
    def solution_676_5_2(self,used,vis,prev,n):
        if used == n: 
            #we reached the end
            self.ans += 1
            return
        tmp = {}
        for i in range(n):
            if vis[i] == False and self.nums[i] not in tmp:
                tmp[self.nums[i]] = True
                if self.nums[i] in self.d[prev]:
                    vis[i] = True
                    self.solution_676_5_2(used+1,vis,self.nums[i],n)
                    vis[i] = False
        
    def solution_676_5_3(self, nums: List[int]) -> int:
        d = { x:{} for x in nums}
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if self.solution_676_5_1(nums[i] + nums[j]):
                    d[nums[i]][nums[j]] = True
                    d[nums[j]][nums[i]] = True
        self.nums = nums
        self.ans = 0
        self.d = d
        vis = [False]*n
        tmp = {}
        for i in range(n):
            if nums[i] in tmp: continue
            tmp[nums[i]] = True
            vis[i] = True
            self.solution_676_5_2(1,vis,self.nums[i],n)
            vis[i] = False
        return self.ans