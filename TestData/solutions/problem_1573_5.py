class Solution:
    def solution_1573_5(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        if len(capacity) == len(rocks) :
            arr = {}
            for i in range(n):
                arr[i] = capacity[i]-rocks[i]
            arr = sorted(arr.values())
            val = additionalRocks
            answer = 0
            for j in range(n):
                if val >= arr[j]:
                    val  = val - arr[j]
                    answer = answer + 1
            return answer