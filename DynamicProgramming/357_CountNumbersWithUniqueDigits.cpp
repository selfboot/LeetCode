/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-08 10:45:15
 */


class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        if(n==0){
            return 1;
        }
        if(n==1){
            return 10;
        }
        if(n==2){
            return 91;
        }
        vector<int> dp(n+1, 0);
        dp[1] = 10;
        dp[2] = 81;
        int result = 91;
        for(int i=3; i<min(11, n+1); i++){
            dp[i] = dp[i-1] * (11-i);
            result += dp[i];
        }
        return result;
    }
};

/*
0
2
9
12
*/
