/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-06-12 23:22:13
 */

class Solution {
public:
     /*
      * Rotate the image by 90 degrees (clockwise).

      * After rotate, the element in A[i][j] moves to A[j][n-1-i].  So we can
      * Firstly reverse up to down : A[i][j]     --> A[n-1-i][j]
      * Then then swap the symmetry: A[n-1-i][j] --> A[j][n-1-i]

      * 1 2 3     7 8 9     7 4 1
      * 4 5 6  => 4 5 6  => 8 5 2
      * 7 8 9     1 2 3     9 6 3
      */
    void rotate(vector<vector<int>>& matrix) {
        reverse(matrix.begin(), matrix.end());
        for(int i=0; i<matrix.size(); i++){
            for(int j=0; j<i; j++){
                swap(matrix[i][j], matrix[j][i]);
            }
        }
    }
};
