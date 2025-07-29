class Solution:
    def solution_932_5_1(self, n: int) -> int:
        def solution_932_5_2(num):
            sum1 = 0
            while num>0:
                sum1+=num%10
                num//=10
            return sum1
        map1 = {}
        maxi = 0
        count = 0
        for i in range(1, n+1):

            s = solution_932_5_2(i)
            if s in map1:
                map1[s]+=1
                if map1[s]>maxi:
                    maxi = map1[s]
            else:
                map1[s]=1
                if map1[s]>maxi:
                    maxi = map1[s]
        
        for elem in map1:
            if map1[elem]==maxi:
                count+=1
        print(map1)
        
        return count