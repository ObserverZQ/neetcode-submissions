class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we can define a tuple to store the row, column, and grid to see if each metric meets expectation. to check duplicates, we use sets for each row, colum and grid.
        # optimal time: O(n2)
        nums = defaultdict(set)
        ROW, COL = len(board), len(board[0])
        for r in range(ROW):
            for c in range(COL):
                grid = str((r // 3, c // 3))
                val = board[r][c]
                if val == '.':
                    continue
                # check row
                if val in nums[str(r)+',_,_']:
                    return False
                nums[str(r)+',_,_'].add(val)
                # check column
                if val in nums['_,'+str(c)+',_']:
                    return False
                nums['_,'+str(c)+',_'].add(val)
                # check grid
                if val in nums['_,_,'+grid]:
                    return False
                nums['_,_,'+grid].add(val)
        return True