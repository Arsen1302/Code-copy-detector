class Solution:
    def solution_1033_5(self, arr: List[int], a: int, b: int, c: int) -> int:
        pre = [0] * 1001
        post = Fenwick(1001)
        pre[arr[0]] += 1
        vi = 2
        while vi < 0 + len(arr):
            # post[arr[vi]] += 1
            post.addSum(arr[vi], 1)
            vi += 1
        # pi = 1 
        # while pi < 0 + len(post):
        #     post[pi] += post[pi-1]
        #     pi += 1
        i = 1
        ans = 0
        while i < 0 + len(arr) - 1:
            middle = arr[i]
            aupper = min(1000, middle + a)
            alower = max(0, middle - a)
            bupper = min(1000, middle + b)
            blower = max(0, middle - b)
            traversea = alower
            while traversea <= aupper:
                if pre[traversea]:
                    intersectlower = max(blower, traversea - c)
                    intersecupper = min(bupper, traversea + c)
                    if intersecupper >= intersectlower:
                        if not intersectlower:
                            # ans += pre[traversea] * post[intersecupper]
                            ans += pre[traversea] * post.getSum(intersecupper)
                        else:
                            # ans += pre[traversea] * (post[intersecupper] - post[intersectlower - 1])
                            ans += pre[traversea] * post.getCum(intersecupper, intersectlower)
                traversea += 1
            pre[middle] += 1
            vaftermiddle = arr[i + 1]
            # while vaftermiddle <= 1000:
            #     post[vaftermiddle] -= 1
            #     vaftermiddle += 1
            post.addSum(vaftermiddle, -1)
            i += 1
        return ans