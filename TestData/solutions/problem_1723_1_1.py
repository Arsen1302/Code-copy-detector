class Solution(object):
    def solution_1723_1_1(self, root, queries):
        def solution_1723_1_2(root, arr):
            if not root: return
            solution_1723_1_2(root.left, arr)
            arr.append(root.val)
            solution_1723_1_2(root.right, arr)
        arr = []
        solution_1723_1_2(root, arr)
        ans = []
        n = len(arr)
        for key in queries:
            left, right = 0, n - 1
            while right >= left:
                mid = (right + left) // 2
                if arr[mid] == key:
                    break
                elif arr[mid] > key:
                    right = mid - 1
                else:
                    left = mid + 1
            if arr[mid] == key:
                ans.append([arr[mid], arr[mid]])
            elif arr[mid] > key:
                if (mid - 1) >= 0:
                    ans.append([arr[mid - 1], arr[mid]])
                else:
                    ans.append([-1, arr[mid]])
            else:
                if (mid + 1) < n:
                    ans.append([arr[mid], arr[mid + 1]])
                else:
                    ans.append([arr[mid], -1])
        return ans