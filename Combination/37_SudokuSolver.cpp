/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-17 13:59:43
 */

class Solution {
private:
    bool rows_hash[9][9];
    bool cols_hash[9][9];
    bool panel_hash[9][9];
    const vector<int> nums_list = {0,1,2,3,4,5,6,7,8};

    bool dfs_search(int pos, vector<vector<char>>& board){
        if(pos==81){
            return true;
        }
        int r = pos / 9, c = pos % 9;
        if(board[r][c] != '.'){
            return dfs_search(pos+1, board);
        }
        else{
            for(const auto& n: nums_list){
                if(put_num(n, r, c)){
                    board[r][c] = '1' + n;
                    if(dfs_search(pos+1, board)){
                        return true;
                    }
                    board[r][c] = '.';
                    backtrack(n, r, c);
                }
            }
            return false;
        }
    }

    bool put_num(int num, int row, int col){
        int panel_pos = row / 3 * 3 + col / 3;
        if(rows_hash[row][num] || cols_hash[col][num] || panel_hash[panel_pos][num]){
            return false;
        }
        rows_hash[row][num] = cols_hash[col][num] = panel_hash[panel_pos][num] = 1;
        return true;
    }

    void backtrack(int num, int row, int col){
        int panel_pos = row / 3 * 3 + col / 3;
        rows_hash[row][num] = cols_hash[col][num] = panel_hash[panel_pos][num] = 0;
    }

public:
    /*
    According to:
    https://discuss.leetcode.com/topic/27787/c-clear-solution-using-dfs-beating-90-c-coder
    */
    void solveSudoku(vector<vector<char>>& board) {
        memset(rows_hash, 0, sizeof(rows_hash));
        memset(cols_hash, 0, sizeof(cols_hash));
        memset(panel_hash, 0, sizeof(panel_hash));

        for(int i=0; i<9; i++){
            for(int j=0; j<9;j++){
                if(board[i][j] != '.'){
                    int num = board[i][j] - '1';
                    put_num(num, i, j);
                }
            }
        }
        dfs_search(0, board);
    }
};
