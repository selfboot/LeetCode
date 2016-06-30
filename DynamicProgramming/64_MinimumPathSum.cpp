/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-06-30 14:48:13
 */

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        if(grid.size()==0){
            return 0;
        }
        int rows = grid.size();
        int cols = grid[0].size();

        vector<vector<int>> dp(rows, vector<int>(cols, 0));
        for(int i=0; i<rows; i++){
            for(int j=0; j<cols; j++){
                dp[i][j] = grid[i][j];
                if(i==0 && j>0){
                    dp[i][j] += dp[i][j-1];
                }
                else if(j==0 && i>0){
                    dp[i][j] += dp[i-1][j];
                }
                else if(j > 0 && i>0){
                    dp[i][j] += min(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        return dp[rows-1][cols-1];
    }
};

/*
[]
[[0]]
[[1,2,4,3,2,1,5],[3,4,1,2,3,5,4],[3,2,4,5,1,2,5]]
*/
