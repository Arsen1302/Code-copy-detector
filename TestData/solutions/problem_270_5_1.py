class Solution:
    def solution_270_5_1(self, num: int) -> int:
	   #Function  to get the binary value
        def solution_270_5_2(n):
            
            if n==0 or n==1:
                return str(n)
            if n%2==0:
                return '0'+solution_270_5_2(n//2)
            else:
                return '1'+solution_270_5_2(n//2)
            
        bin_=[i for i in solution_270_5_2(num) ]
		
		#invert the bits
        for i in range(len(bin_)):
            if bin_[i]=='0':
                bin_[i]=1
            else:
                bin_[i]=0
				
        #converting binary value to decimal value        
        def solution_270_5_3():
            ans=0
            for i in range(len(bin_)):
                ans=ans+(2**i)*bin_[i]
            return ans
        return solution_270_5_3()