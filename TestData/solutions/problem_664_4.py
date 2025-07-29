class Solution:
    def solution_664_4(self, a: int, b: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        
        s = ''
        while heap:
            try:
                curr_char_remain, current_char = heapq.heappop(heap)
            except IndexError:
                break
            curr_char_remain = abs(curr_char_remain)
            if s[-2:] != 2 * current_char:
                if curr_char_remain >= 2:
                    s += 2 * current_char
                    curr_char_remain -= 2
                    if curr_char_remain > 0:
                        heapq.heappush(heap, (-1 * curr_char_remain, current_char))
                else:
                    s += current_char
            else:
                try:
                    n_curr_char_remain, n_current_char = heapq.heappop(heap)
                except IndexError:
                    break
                n_curr_char_remain = abs(n_curr_char_remain)
                s += n_current_char
                n_curr_char_remain -= 1
                if n_curr_char_remain != 0:
                    heapq.heappush(heap, (-1 * n_curr_char_remain, n_current_char))
                heapq.heappush(heap, (-1 * curr_char_remain, current_char))
        return s