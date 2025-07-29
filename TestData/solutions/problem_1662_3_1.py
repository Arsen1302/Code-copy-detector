class Solution:
    def solution_1662_3_1(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = [0] * n
        def solution_1662_3_2(meeting):
            result = None
            for i in range(n):
                if rooms[i] <= meeting[0]:
                    rooms[i] = meeting[1]
                    result = i
                    break
            if result is None:
                minVal = min(rooms)
                result = rooms.index(minVal)
                rooms[result] += meeting[1] - meeting[0]
            return result
        
        frequences = [0] * n
        for meeting in meetings:
            index = solution_1662_3_2(meeting)
            frequences[index] += 1
        return frequences.index(max(frequences))