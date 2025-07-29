class Solution:
    def solution_932_3_1(self, n: int) -> int:
        def solution_932_3_2():
            return 0
			
        dic = defaultdict(solution_932_3_2)
		
        for i in range(1,n+1):
            st = str(i)
            ans = 0
			
            for j in st:
                ans += int(j)
				
            dic[ans] += 1
			
        maximum = max(dic.values())
        ans = 0 
		
        for i in dic.keys():
            if dic[i] == maximum:
                ans += 1
				
        return ans