/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-10-09 14:22:17
 */

class Solution {
public:
    /*
    dp[i][j] is the j-th position's minimum path sum in i-th row.
    Then we can find the recursive formula:
        dp[i][j] = min(dp[i-1][j-1] if j-1>=0, dp[i-1][j]) + triangle[i][j]
    */
    int minimumTotal(vector<vector<int>>& triangle) {
        int rows = triangle.size();
        if(rows==0 || triangle[0].size()==0){
            return 0;
        }

        std::vector<int> dp(rows, 0);
        for(auto lines : triangle){
            for(int i=lines.size()-1; i!=-1; i--){
                if(i-1>=0 && dp[i-1]<dp[i] || (i==lines.size()-1)){
                    dp[i] = dp[i-1] + lines[i];
                }
                else{
                    dp[i] += lines[i];
                }
            }
        }
        int min_path_sum = dp[0];
        for(int i=1; i<rows; i++){
            min_path_sum = dp[i] < min_path_sum ? dp[i] : min_path_sum;
        }
        return min_path_sum;
    }
};

/*
[]
[[-10]]
[[2],[3,4],[6,5,7],[1,4,8,3]]
[[2],[3,3],[1,5,0],[4,6,9,3]]
*/
