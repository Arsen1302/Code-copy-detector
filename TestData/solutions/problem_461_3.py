class Solution:
    def solution_461_3(self, s: str) -> str:
        counter = {}
        for ch in s:
            if ch in counter:
                counter[ch] +=1
            else:
                counter[ch] = 1
        queue = []
        
        for elem in counter:
            heapq.heappush(queue, (-1*counter[elem], elem))
            
        result = []
        prev_char = None
        prev_freq = None
        while(queue):
            freq, elem  = heapq.heappop(queue)
            result.append(elem)
            if prev_freq:
                # it makes sure that character whihc is popped just now is not popped next, i.e. maintains non- adjacent condition
                heapq.heappush(queue, (prev_freq, prev_char))
            
            prev_char, prev_freq = elem, freq + 1 # +1 is equivalent to -1 as we used max_heap
        if len(result) == len(s):
            return "".join(result)
        return ""