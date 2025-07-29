class Solution:
    def solution_1233_1_1(self, nums: List[int]) -> int:
        
        # define constants
        n = len(nums)
        MOD = 10**9 + 7
        
        # handle scenario for no pairs
        if n<=1:
            return 0
        
        # utility method to calculate reverse of a number
        # e.g. solution_1233_1_2(123) -> 321
        def solution_1233_1_2(i):
            new = 0
            while(i!=0):
                r = i%10
                new = new*10+r
                i = i//10
            return new
        
        # calculate frequency of all the diffs
        freq_counter = defaultdict(int)
        for num in nums:
            freq_counter[num-solution_1233_1_2(num)] += 1
        
        # for all the frequencies calculate the number of paris
        # which is basically nC2 (read as - "n choose 2") -> n*(n-1)/2
        answer = 0
        for freq in freq_counter.keys():
            count = freq_counter[freq]
            # note the modulo operation being performed to handle large answer
            answer = (answer + (count*(count-1))//2)%MOD
                          
        return answer