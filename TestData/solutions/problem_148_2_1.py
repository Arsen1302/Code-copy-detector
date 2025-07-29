class Solution:
    def solution_148_2_1(self, num: str):
        return self.solution_148_2_2(num)

    def solution_148_2_2(self, num: str):
        path = []

        def solution_148_2_2(cur_str, cut_size) -> bool:
            ''' retval means: found '''

            # not additive
            if cut_size >= 3 and path[-1] != path[-2] + path[-3]: return False

            # end
            if cur_str == '': return cut_size >= 3

            # solution_148_2_2
            for cur_idx in range(1, len(cur_str) + 1):
                cut_str, remain = cur_str[:cur_idx], cur_str[cur_idx:]

                # check start 0
                if cut_str.startswith('0') and cut_str != '0': break

                path.append(int(cut_str))

                if solution_148_2_2(remain, cut_size + 1): return True

                path.pop()  # recover

            return False

        return solution_148_2_2(num, 0)