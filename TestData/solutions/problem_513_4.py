class Solution:
    def solution_513_4(self, ages: List[int]) -> int:
        
        # make a number sort
        sort_ages = [0]*120
        
        # sort the ages
        for age in ages:
            sort_ages[age-1] += 1
            
        # make prefix sum
        for age in range(2,121):
            sort_ages[age-1] = sort_ages[age-1] + sort_ages[age-2]
            
        # make a sliding window through the array
        result = 0
        for age in ages:
            
            # these ages fall out due to the first restriction
            # 14//2 + 7 = 14 -> 14 <= 14 -> falls out
            if age <= 14:
                continue
            
            # calculate the index of persons we don't want
            dox = age//2 + 7
            
            # this is the amount of persons younger than ourselves
            # but older than age//2 + 7
            result += sort_ages[age-2] - sort_ages[dox-1]
            
            # this is the amount of persons the same age as us but
            # without ourselves as we don't send a request to ourself
            result += (sort_ages[age-1] - sort_ages[age-2]) - 1
        
        return result