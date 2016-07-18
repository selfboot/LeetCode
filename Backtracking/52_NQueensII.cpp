/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-18 16:31:27
 */

class Solution {
public:
    int totalNQueens(int n) {
        vector<bool> cols(n, true);
        vector<bool> left_right(2*n-1, true);
        vector<bool> right_left(2*n-1, true);
        int count = 0;
        solveNQueens(0, cols, left_right, right_left, count);
        return count;
    }
private:
    /*
    Refer to:
    https://discuss.leetcode.com/topic/13617/accepted-4ms-c-solution-use-backtracking-and-bitmask-easy-understand
    The number of columns is n, the number of 45° diagonals is 2 * n - 1,
    the number of 135° diagonals is also 2 * n - 1.
    When reach [row, col], the column No. is col,
    the 45° diagonal No. is row + col and the 135° diagonal No. is n - 1 + col - row.

    | | |                / / /             \ \ \
    O O O               O O O               O O O
    | | |              / / / /             \ \ \ \
    O O O               O O O               O O O
    | | |              / / / /             \ \ \ \
    O O O               O O O               O O O
    | | |              / / /                 \ \ \
   3 columns        5 45° diagonals     5 135° diagonals    (when n is 3)
    */
    void solveNQueens(int row, vector<bool> &cols, vector<bool> &lr, vector<bool> &rl, int &count){
        if(row==cols.size()){
            count ++;
            return;
        }
        for(int i=0; i<cols.size(); i++){
            if(cols[i] && lr[row+cols.size()-1-i] && rl[row+i]){
                cols[i] = lr[row+cols.size()-1-i] = rl[row+i] = false;
                solveNQueens(row+1, cols, lr, rl, count);
                cols[i] = lr[row+cols.size()-1-i] = rl[row+i] = true;
            }
        }
    }
};

/*
1
2
8
*/
