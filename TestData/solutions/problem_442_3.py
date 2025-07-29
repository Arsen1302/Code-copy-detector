class Solution:
    def solution_442_3(self, nums: List[int]) -> int:
# createed a dic to store value of a number i.e the dic[n] =  n*(number of times it occurs)
        dic = defaultdict(int)
        for n in nums:
            dic[n] += n
# made a list of unique num in nums, OR -> made a list so we can use it as House Robber  
        newList = list(set(nums))
        newList.sort()
        
# point list contains all the indexes in newList where the difference between any two consicutive num is greater than 1.
# newList = [2,3,4,6,7,8,11,12] then -> point = [3,6] + ( also append len(newList)) to process the last 11,12 as we did in House Robber.
# points = [3,6,8]
        point = []
        N = len(newList)
        for i in range(1,N):
            if newList[i] - newList[i-1] > 1:
                point.append(i)
        if len(point)==0 or point[-1] != N:
            point.append(N)

# similar to House Robber. We try to get maximum for each sub array.
# [2,3,4] , [6,7,8] , [11,12]  ( prev = 0 )

        earning,prev = 0,0 # earning = 0, prev = 0 ( index starting)
        for indx in point:  # points = # points = [3,6,8].. for each index we want to calculate max contiribution of it subarray... [0,3], [3,6], [6,8]
            dp = [-10**20,-10**20]
            for i,n in enumerate(newList[prev:indx]): # lists -> [2,3,4] , [6,7,8] , [11,12]  
                if i == 0: # BASE CONDITION 
                    dp[0] = max(dp[0], dic[n]) 
                    continue
                if i == 1: # BASE CONDITION 
                    dp[1] = max(dp[1], dic[n])
                    continue
                # UPDATING VALUES
                temp = dp[1]
                dp[1] = max(dic[n], dp[0]+dic[n],dp[1])
                dp[0] = max(temp,dp[0])        
            earning += max(dp) # updating earings
            prev = indx #prev updated to 3,6,8 after subarrays
        
        return earning # FINAL ANSWER