class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        sets = defaultdict(set)

        for row in range(9):
            for column in range(9):
                if board[row][column] == ".": continue
                square = int(row / 3) * 3 + int(column / 3)
                value = board[row][column]
                if (value not in sets[f'row{row}'] and 
                value not in sets[f'column{column}'] and 
                value not in sets[f'square{square}']):
                    sets[f'row{row}'].add(value)
                    sets[f'column{column}'].add(value)
                    sets[f'square{square}'].add(value)
                else:
                    return False
        
        return  True
        