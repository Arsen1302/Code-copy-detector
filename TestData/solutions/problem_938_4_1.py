class Solution:
    def solution_938_4_1(self, a: int, b: int, c: int) -> str:
        substr = ""
        options = {
            "a": a,
            "b": b,
            "c": c
        }
        
        def solution_938_4_2(x):
            if substr[-2:] + x not in {'aaa', 'bbb', 'ccc'}:
                return True
            return False

        while options["a"] > 0 or options["b"] > 0 or options["c"] > 0:
            max_order = {
                k: v 
                for k, v in sorted(
                    options.items(), key=lambda item: -item[1])
            }
            for k, v in max_order.items():
                if solution_938_4_2(k) and v > 0:
                    options[k] -= 1
                    substr += k
                    break
            else:
                break
        
        return substr