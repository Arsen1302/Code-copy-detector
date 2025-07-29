class Solution:
    def solution_575_4(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        total_alice=sum(aliceSizes)
        total_bob=sum(bobSizes)
        diff=(total_alice-total_bob)//2
        
        for i in set(aliceSizes):
            if i-diff in set(bobSizes):
                return [i,i-diff]
            

		```