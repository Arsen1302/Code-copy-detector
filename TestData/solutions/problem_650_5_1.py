class Solution:
    def solution_650_5_1(self, arr: List[int]) -> List[int]:
        i=0
        n=len(arr)
        kArr=[]
        sorted = 0
        while i<n:
            if not self.solution_650_5_2(arr):
                k=self.solution_650_5_3(arr[:n-sorted])
                if k != 0:
                    kArr.append(k+1)
                    arr = self.solution_650_5_4(arr, k)
                arr = self.solution_650_5_4(arr, n-1-sorted)
                kArr.append(n-sorted)
                sorted+=1
            else:
                return kArr
            
    
    def solution_650_5_2(self, arr):
        arr1 = arr[:]
        arr1.sort()
        print(arr1==arr)
        return arr1 == arr
    
    def solution_650_5_3(self, arr):
        m = arr.index(max(arr))
        print(m)
        return m
    
    def solution_650_5_4(self, arr, k):
        print(arr[:k+1][::-1] + arr[k+1:])
        return arr[:k+1][::-1] + arr[k+1:]