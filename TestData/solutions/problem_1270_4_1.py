class Solution:
    def solution_1270_4_1(self, s: str) -> int:
	
		# for odd length string with number of 1s > number of 0s it should be starting with 1
		# while for number of 0s > number of 1s it should be starting with 0
		# If abs diff of number of 1s and 0s is greater than 1 then we can't make it alternating
        one = s.count("1")
        zero = s.count("0")
        
        if (abs(one-zero) > 1):
            return -1
        
        def solution_1270_4_2(s, ch):
            res = 0
            for i in range(len(s)):
                if (ch!= s[i]):
                    res += 1
                    
                if ch == "1":
                    ch = "0"
                else:
                    ch = "1"
                    
            return res // 2
        
        if zero > one:
            return solution_1270_4_2(s, "0")
        elif (one > zero):
            return solution_1270_4_2(s, "1")
        else:
             return min(solution_1270_4_2(s, "0"), solution_1270_4_2(s, "1"))