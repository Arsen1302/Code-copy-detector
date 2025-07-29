class Solution:
    def solution_704_2(self, clips: List[List[int]], time: int) -> int:
        if (time == 0): return 0
        clips.sort(key=lambda i: (i[0], -i[1]))
        output = [clips[0]]
        start, end = output[-1][0], output[-1][1]
        
        for currStart, currEnd in clips[1:]:
            if (currStart <= end <= currEnd and end < time):
                # pop the last clip if the second last clip overlaps with current clip and current clip is longer than the last clip
                if (len(output) > 1 and currStart <= output[-2][1]):
                    output.pop()
                start = min(start, currStart)
                end = max(end, currEnd)
                output.append([currStart, currEnd])

        
        if (start <= 0 and end >= time):
            return len(output)
        else:
            return -1