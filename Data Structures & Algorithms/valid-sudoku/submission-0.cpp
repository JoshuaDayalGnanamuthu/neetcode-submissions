class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map <int, unordered_set<char>> rows;
        unordered_map <int, unordered_set<char>> columns;
        unordered_map <int, unordered_set<char>> squares;

        for (int i {0}; i < board.size(); i++){
            for (int j {0}; j < board[i].size(); j++){
                if (board[i][j] == '.') continue;
                
                if (rows[i].count(board[i][j])) return false;
                rows[i].insert(board[i][j]);
                
                int index = (i/3) * 3 + (j/3);
                if (squares[index].count(board[i][j])) return false;
                squares[index].insert(board[i][j]);
                
                if (columns[j].count(board[i][j])) return false;
                columns[j].insert(board[i][j]);


            }
        }
        return true;
    }
};
