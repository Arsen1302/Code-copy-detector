class Solution:
    def solution_429_2_1(self, accounts: List[List[str]]) -> List[List[str]]:
        def solution_429_2_2(x):
            if parent[x] != x:
                parent[x] = solution_429_2_2(parent[x])
            return parent[x]
        def solution_429_2_3(x, y):
            rootx = solution_429_2_2(x)
            rooty = solution_429_2_2(y)
            if rootx == rooty:
                return
            if rank[rootx] > rank[rooty]:
                parent[rooty] = rootx
            elif rank[rooty] > rank[rootx]:
                parent[rootx] = rooty
            else:
                parent[rootx] = rooty
                rank[rooty] += 1
        parent = list(range(len(accounts)))
        rank = [0] * len(accounts)
        email_parent = {}
        for idx, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_parent:
                    solution_429_2_3(idx, email_parent[email])
                email_parent[email] = idx
        ans = {}
        for email in email_parent:
            root = solution_429_2_2(email_parent[email])
            if root in ans:
                ans[root].append(email)
            else:
                ans[root] = [accounts[root][0], email]
        ans = list(ans.values())
        for account in ans:
            account[1:] = sorted(account[1:])
        return ans