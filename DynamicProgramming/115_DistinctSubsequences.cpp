/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-10-09 12:06:21
 */

class Solution {
public:
    /*
    dp[i][j] is the number of ways to remove some characters
    from S[0,i] to get T[0,j], we have the recursive formula:
    dp [i][j] = dp[i-1][j] if S[i] != T[j] ,
    or dp [i][j] = dp[i-1][j] + dp[i-1][j-1] if S[i] ==T[j]
    */
    int numDistinct(string s, string t) {
        if(s=="" || t==""){
            return 0;
        }

        int s_len = s.size();
        int t_len = t.size();
        if(s_len == t_len && s != t || (s_len < t_len)){
            return 0;
        }

        /*
        dp[i][j] refer to only dp[i-1][j] and dp[i-1][j-1].
        This gives us the idea that we can reduce the space to O(n).
        Since we need to make use of dp[i-1][j-1], we run backward!!!
        */
        std::vector<int> dp(t_len+1, 0);
        dp[0]=1;
        for(int i=1; i<s_len+1; i++){
            for(int j=t_len; j>0; j--){
                if(s[i-1] == t[j-1]){
                    dp[j] += dp[j-1];
                }
            }
        }

        return dp[t_len];
    }
};

/*
""
"a"
"ababcc"
"abc"
"rabbbit"
"rabbit"
*/
