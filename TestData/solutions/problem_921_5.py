class Solution:
    def solution_921_5(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        distance = len(arr1)
        for num in arr1:
            start = 0
            end = len(arr2) - 1
            while start <= end:
                mid = (start+end)//2
                if abs(num- arr2[mid]) <= d:
                    distance -= 1
                    break
                elif arr2[mid] > num :
                    end = mid-1
                elif arr2[mid] < num :
                    start = mid+1
        return distance