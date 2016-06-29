/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-06-29 11:13:07
 */

class Solution {
public:
    int uniquePaths(int m, int n) {
        /*
        Using formula.

        Choose (n - 1) movements(number of steps to the right) from (m + n - 2),
        and rest (m - 1) is (number of steps down).
        We calculate the total possible path number
        Combination(N, k) = n! / (k!(n - k)!)
        reduce the numerator and denominator and get
        C = ( (n - k + 1) * (n - k + 2) * ... * n ) / k!
        */
        double path_cnt = 1;
        int N = m+n-2;
        int K = m < n ? m-1 : n-1;
        for(int i=1; i<=K; i++){
            path_cnt = path_cnt * (N-K+i) / i;
        }
        return int(path_cnt);
    }
};


class Solution_2{
public:
    int uniquePaths(int m, int n) {
        // Dynamic Programming.
        // According to:
        // https://leetcode.com/discuss/38353/0ms-5-lines-dp-solution-in-c-with-explanations
        vector<vector<int> > dp(m, vector<int>(n, 1));
        for(int i=1; i< m; i++){
            for(int j=1; j<n; j++){
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
};


/*
0
5
3
8
87
99
*/
