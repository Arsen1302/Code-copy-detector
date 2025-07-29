class Solution:
    def solution_1408_3(self, head: Optional[ListNode]) -> List[int]:
        i = prev_val = first_critical_idx = prev_critical_idx = critical_idx = 0
        min_diff = inf
        found_two_critical = False
        while head:
            if i == 0:
                prev_val = head.val
            elif head.next:
                new_critical = False
                if head.val < head.next.val:
                    if head.val < prev_val:
                        critical_idx = i
                        new_critical = True
                elif head.val > head.next.val:
                    if head.val > prev_val:
                        critical_idx = i
                        new_critical = True

                if new_critical:
                    if not first_critical_idx:
                        first_critical_idx = prev_critical_idx = critical_idx
                    else:
                        min_diff = min(min_diff,
                                       critical_idx - prev_critical_idx)
                        prev_critical_idx = critical_idx
                        found_two_critical = True
                prev_val = head.val
            head = head.next
            i += 1
        return ([min_diff, critical_idx - first_critical_idx]
                if found_two_critical else [-1, -1])