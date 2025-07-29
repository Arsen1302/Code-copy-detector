class Solution:
    def solution_349_4(self, f: str) -> str:
    	f, d = [int(i) for i in (f.replace('/',' ').replace('+',' +').replace('-',' -')).split()], 1
    	for i in range(1,len(f),2): d *= f[i]
    	return (lambda x,y: str(x//math.gcd(x,y))+"/"+str(y//math.gcd(x,y)))(sum(d*f[i]//f[i+1] for i in range(0,len(f),2)),d)
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com