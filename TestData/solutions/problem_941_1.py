class Solution:
    def solution_941_1(self, queries: List[int], m: int) -> List[int]:
        permuteArr=[i for i in range(1,m+1)]
        query_len=len(queries)
        answer=[]
        left,right=[],[]
        for query in range(query_len):
            index=permuteArr.index(queries[query])
            answer.append(index)
            left=permuteArr[:index]
            right=permuteArr[index+1:]
            permuteArr=[permuteArr[index]]+left+right
        return answer