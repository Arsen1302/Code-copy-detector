class Solution:
    def solution_139_4_1(self, num: str, target: int) -> List[str]:
        ret = []
        def solution_139_4_2(subtotal, last, path, start):
            if start == len(num):
                if subtotal == target:
                    ret.append(''.join(path))
                return
            for i in range(start, len(num)):
                ch = num[start:i + 1]
                if len(ch) > 1 and ch[0] == '0':
                    continue
                integer = int(ch)
                if not path:
                    solution_139_4_2( integer, integer, [ch], i + 1 )
                else:
                    solution_139_4_2( subtotal + integer, integer, path + ['+', ch], i + 1 )
                    solution_139_4_2( subtotal - integer, -integer, path + ['-', ch],i + 1 )
					# the most interesting part:
					# e.g. 1+2*3, we record last as 2, so: 3-2+2*3 = 7
                    solution_139_4_2( subtotal - last + last * integer, last * integer, path + ['*', ch], i + 1 ) 
        solution_139_4_2(0, 0, [], 0)
        return ret