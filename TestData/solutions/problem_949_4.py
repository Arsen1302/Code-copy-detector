class Solution:
    def solution_949_4(self, orders: List[List[str]]) -> List[List[str]]:
        dummy_cnts = [0]
        unique_tbl_no = []
        items = []
        d = {}
        for i in orders:
            tbl_item = (i[1], i[2])
            if int(i[1]) not in unique_tbl_no:
                unique_tbl_no.append(int(i[1]))
            if i[2] not in items:
                items.append(i[2])
                dummy_cnts.append(0)
            if tbl_item not in d:
                d[tbl_item] = 1
            else:
                d[tbl_item] += 1

        items = sorted(items)
        final_list = [items]
        final_list[0].insert(0, "Table")
        for table_no in sorted(unique_tbl_no):
            table_no = str(table_no)
            nested_lst = dummy_cnts.copy()
            for item in items:
                index_for_cnts = items.index(item)
                nested_lst[0] = table_no
                nested_lst[index_for_cnts] = str(d.get((table_no, item), 0))
            final_list.append(nested_lst)
        return final_list