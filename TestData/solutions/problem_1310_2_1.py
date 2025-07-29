class Solution:
    def solution_1310_2_1(self, dist: List[int], speed: List[int]) -> int:
        
		def solution_1310_2_2(a):
            return a[0]/a[1]
        
		temp = []
        for i in range(len(dist)):
            temp.append([dist[i],speed[i]])
        temp = sorted(temp,key = solution_1310_2_2)
        ans = 0
        i = 0

        while i<len(temp):
            if (temp[i][0] - (temp[i][1])*i) > 0 :
                ans += 1
                i += 1
            else:
                break
        return ans