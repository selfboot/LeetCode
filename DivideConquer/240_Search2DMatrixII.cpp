/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-13 11:50:05
 */

class Solution {
public:
    /*
    O(m+n)
    Check the top-right corner.
    If it's not the target, then remove the top row or rightmost column.
    */
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.empty()){
            return false;
        }
        int m_rows = matrix.size(), n_cols = matrix[0].size();
        int top=0, right=n_cols-1;
        while(top<m_rows && right>=0){
            if(matrix[top][right] > target){
                right -= 1;
            }
            else if(matrix[top][right] < target){
                top += 1;
            }
            else{
                return true;
            }
        }
        return false;
    }
};

/*
[[]]
0
[[-5]]
-2
[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24]]
12
*/
