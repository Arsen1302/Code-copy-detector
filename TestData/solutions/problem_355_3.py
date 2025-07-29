class Solution:
    def solution_355_3(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.append(0)
        l=flowerbed
        for i in range(len(l)-1):
            if l[i-1]+l[i]+l[i+1]==0:
                l[i]=1
                n-=1 
        print(l[-1]+l[0]+l[1])
        return n<=0