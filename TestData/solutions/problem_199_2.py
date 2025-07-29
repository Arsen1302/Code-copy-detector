class Solution:
    def solution_199_2(self, input: str) -> int:
        max_len,ht = 0,{}
        for p in input.split("\n"):
            key=p.count("\t")
            if "." not in p:
                value = len(p.replace("\t",""))
                ht[key]=value
            else:
                temp_len = key + len(p.replace("\t",""))
                for ky in ht.keys():
                    if ky < key:
                        temp_len += ht[ky]
                max_len=max(max_len,temp_len)
        return max_len