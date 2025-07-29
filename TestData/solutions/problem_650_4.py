class Solution:
    def solution_650_4(self, arr: List[int]) -> List[int]:
        n = len(arr)
        issorted = True
        for i in range(1,n):
            if arr[i] < arr[i-1] :
                issorted = False
                break
        if issorted == True : return []
        
        flips = []
        for i in range(n):
            if len(flips) > 10 * n : return [-1]
            maxx = 0
            for j in range(n-i):
                if arr[j] > arr[maxx] : maxx = j
            if maxx != 0 :
                flips.append(maxx+1)
                low = 0
                high = maxx
                while low < high:
                    arr[low],arr[high] = arr[high],arr[low]
                    high -= 1
                    low  += 1
            low = 0
            high = n - i - 1
            while low < high :
                arr[low] , arr[high] = arr[high] , arr[low]
                low += 1
                high -= 1
            flips.append(n-i)
        return flips