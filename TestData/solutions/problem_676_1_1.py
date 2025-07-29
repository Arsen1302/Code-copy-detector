class Solution(object):
    def solution_676_1_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def solution_676_1_2(temp,num,count = 0):
            if len(num)==0:
                return count+1
            for i in xrange(len(num)):
                if (i>0 and num[i]==num[i-1]) or (len(temp) > 0 and math.sqrt(num[i] + temp[-1]) % 1 != 0):
                    continue
                count = solution_676_1_2(temp+[num[i]],num[:i]+num[i+1:],count)
            return count
        
        nums.sort()
        res = solution_676_1_2([],nums)
        return res