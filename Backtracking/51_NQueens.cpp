/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-18 19:42:32
 */

class Solution {
public:
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
    vector<vector<string>> solveNQueens(int n) {
        vector<bool> cols(n, true);
        vector<bool> left_right(2*n-1, true);
        vector<bool> right_left(2*n-1, true);
        string original = string(n, '.');
        vector<string> queueMatrix(n, original);
        vector<vector<string>> ans;
        solve(0, queueMatrix, ans, cols, left_right, right_left, n);
        return ans;
    }

private:
    void solve(int row, vector<string> &matrix, vector<vector<string>> &ans,
               vector<bool> &cols, vector<bool> &left_right, vector<bool> &right_left, int n){
        if(row==n){
            // Get one Queen Square
            ans.push_back(matrix);
            return;
        }

        for(int i=0; i<n; i++){
            if(cols[i] && left_right[n+i-row+1] && right_left[row+i]){
                matrix[row][i] = 'Q';
                cols[i] = left_right[n+i-row+1] = right_left[row+i] = false;
                // Solve the child question.
                solve(row+1, matrix, ans, cols, left_right, right_left, n);
                // Backtracking here.
                matrix[row][i] = '.';
                cols[i] = left_right[n+i-row+1] = right_left[row+i] = true;
            }
        }
    }
};

/*
1
5
8
*/
