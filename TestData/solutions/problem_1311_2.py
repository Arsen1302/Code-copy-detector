class Solution:
def solution_1311_2(self, n: int) -> int:
    MOD = 10**9+7
	
	# No. of even places
    if n%2==0:
        ne=n//2
    else:
        ne=(n+1)//2
    # No. of odd places
    no=n//2
    
    te = pow(5,ne,MOD)      #Total number of even places combinations.
    tp = pow(4,no,MOD)      #Total number of odd/prime combinations.
    return (tp*te)%MOD