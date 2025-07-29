class Solution:
    def solution_1447_4_1(self, arr: List[int], k: int) -> int:
        
        def solution_1447_4_2(nums):
            res = []
            for i in nums:
                low,high = 0, len(res)
                while low < high:
                    mid = (low+high)//2
                    
                    if res[mid] <= i:
                        low = mid + 1
                        
                    else:
                        
                        high = mid


                if low == len(res):
                    res.append(i)
                else:

                    res[low] = i
                    
                    


            return len(res)
        
        ans = 0
                
        
        for i in range(k):
            bucket = []
            startingIdx = i
            while startingIdx < len(arr):
                bucket.append(arr[startingIdx])
                startingIdx += k
                
            
                
                
            ans += len(bucket) - solution_1447_4_2(bucket)
                
                
        return ans
                ```