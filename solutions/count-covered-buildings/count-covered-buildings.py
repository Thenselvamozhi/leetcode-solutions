class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        from collections import defaultdict
        rows = defaultdict(list)
        cols = defaultdict(list)

        for x, y in buildings:
            rows[y].append(x)
            cols[x].append(y)
        
        for y in rows:
            rows[y].sort()
        for x in cols:
            cols[x].sort()
        
        count = 0

        for x, y in buildings:
            row_list = rows[y]
            col_list = cols[x]

            if (x != row_list[0] and x != row_list[-1] and y != col_list[0] and y != col_list[-1]):
                count += 1
        return count