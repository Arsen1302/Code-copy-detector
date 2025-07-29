class Solution:
    #Time-Complexity: O(n^2 + n^2log(n^2)) -> O(n^2*log(n^2)) ->O(n^2*log(n))
    #Space-Complexity: O(n^2)
    def solution_476_4(self, arr: List[int], k: int) -> List[int]:
        array = []
        for i in range(0, len(arr)-1):
            numerator = arr[i]
            for j in range(i+1, len(arr)):
                denominator = arr[j]
                division = numerator / denominator
                array.append([numerator, denominator, division])
        array.sort(key = lambda x : x[2])
        ans = []
        ans.append(array[k-1][0])
        ans.append(array[k-1][1])
        return ans