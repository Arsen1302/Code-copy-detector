class Solution:
    def solution_442_4(self, nums: List[int]) -> int:
	# c
        dic = defaultdict(int)
        for n in nums:
            dic[n] += n
            
        newList = list(set(nums))
        newList.sort()
        
        point = []
        N = len(newList)
        for i in range(1,N):
            if newList[i] - newList[i-1] > 1:
                point.append(i)
        if len(point)==0 or point[-1] != N:
            point.append(N)
       
        earning,prev = 0,0
        for indx in point:
            dp = [-10**20,-10**20]
            for i,n in enumerate(newList[prev:indx]):
                if i == 0:
                    dp[0] = max(dp[0], dic[n])
                    continue
                if i == 1:
                    dp[1] = max(dp[1], dic[n])
                    continue
                temp = dp[1]
                dp[1] = max(dic[n], dp[0]+dic[n],dp[1])
                dp[0] = max(temp,dp[0])
            earning += max(dp)
            prev = indx
        
        return earning