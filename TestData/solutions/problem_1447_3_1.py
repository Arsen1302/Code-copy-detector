class Solution:
    def solution_1447_3_1(self, start):
        results = []
        total = 0
        for i in range(start, len(self.arr), self.k):
            total += 1
            if not results or results[-1] <= self.arr[i]:
                results.append(self.arr[i])
            else:
                results[bisect_right(results, self.arr[i])] = self.arr[i]
        return total - len(results)
            
    def solution_1447_3_2(self, arr: List[int], k: int) -> int:
        self.arr, self.k = arr, k
        return sum(self.solution_1447_3_1(i) for i in range(k))