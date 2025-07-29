class Solution:
    def solution_1719_1_1(self, nums: List[int], k: int) -> int:
        def solution_1719_1_2(num1, num2):
            if(num1>num2):
                num = num1
                den = num2
            else:
                num = num2
                den = num1
            rem = num % den
            while(rem != 0):
                num = den
                den = rem
                rem = num % den
            gcd = den
            lcm = int(int(num1 * num2)/int(gcd))
            return lcm
        count=0
        for i in range(len(nums)):
            lcm=1
            for j in range(i,len(nums)):
                lcm=solution_1719_1_2(nums[j],lcm)
                
                if lcm==k:
                    count+=1
                if lcm>k:
                    break
        return count