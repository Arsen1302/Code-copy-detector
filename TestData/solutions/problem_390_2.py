class Solution:
    def solution_390_2(self, n: int, k: int) -> List[int]:
        number_tail = k // 2
        start, end = [i for i in range(1, n - number_tail + 1)], [i for i in range(n, n - number_tail, -1)]
        i, j = 0, 0
        if k % 2 == 0:
            start, end = end, start
        answer = []
        for i, j in zip(start, end):
            answer.append(i)
            answer.append(j)
        if len(start) > len(end):
            for i in range(len(end), len(start)):
                answer.append(start[i])
        if len(start) < len(end):
            for i in range(len(start), len(end)):
                answer.append(end[i])
        return answer