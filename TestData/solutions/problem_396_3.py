class Solution:
    def solution_396_3(self, nums: List[int]) -> int:

        longestDict = {}

        max_len = 1
        max_cnt = 1
        total_cnt = 0
        for i in range(len(nums)):
            # length of LIS and count of LIS
            longestDict[i] = [1, 1]

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    
                    # found another instance of present LIS length
                    if longestDict[i][0] == longestDict[j][0] + 1:
                        # increase the LIS count at i's position
                        longestDict[i][1] += longestDict[j][1]

                    # check if length of LIS could be more than current
                    elif longestDict[i][0] < longestDict[j][0] + 1:
                        # update length
                        longestDict[i][0] = longestDict[j][0] + 1
                        # since length increased update count to j's count
                        longestDict[i][1] = longestDict[j][1]

                        max_len = max(longestDict[i][0], max_len)

        for LIS_size, LIS_count in longestDict.values():
            if LIS_size == max_len:
                total_cnt += LIS_count

        return total_cnt