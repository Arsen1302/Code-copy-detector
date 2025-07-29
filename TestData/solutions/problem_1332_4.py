class Solution:
    def solution_1332_4(self, milestones: List[int]) -> int:
        '''
        [1 2 5]
        largest_num = 5
        rest_sm = 3(sum(milestones)-max(milestones))
        
        ans = rest_sum*2
        if sum(milestones)-ans >= 1:
            return count+1
        return sum(milestones)  #becuase if all milestones are achieved then it will be simply sum of all
            
        else:
        return count + 1
       
        '''
        largMilestone = max(milestones)
        sumOfAllMilestones = sum(milestones)
        
        sumOfRestMilestone = sumOfAllMilestones - largMilestone
        
        val = sumOfRestMilestone*2
        if sumOfAllMilestones - val >= 1:
            return val+1
        
        return sumOfAllMilestones