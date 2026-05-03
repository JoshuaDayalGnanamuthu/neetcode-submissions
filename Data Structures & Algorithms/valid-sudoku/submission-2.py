class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        hashset = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": continue
                row, column = i, j;
                square = int(row / 3) * 3 + int(column / 3)

                if (board[i][j] not in hashset[f'row{i}'] and 
                board[i][j] not in hashset[f'column{j}'] and 
                board[i][j] not in hashset[f'square{square}']):
                    hashset[f'row{i}'].add(board[i][j])
                    hashset[f'column{j}'].add(board[i][j])
                    hashset[f'square{square}'].add(board[i][j])
                else:
                    return False
        return True
        