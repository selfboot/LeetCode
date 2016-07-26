/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-26 11:48:04
 */

class Solution {
public:
    /*
    Dynamic Programming

    dp[i][j] represents isMatch(p[0...i-1], s[0...j-1]), default is False;
    dp[i][0]: isMatch(p[0...i], ""), dp[0][j]: isMatch("", s[0...j])
    dp[0][0] represents

    If p[i] is "*", dp[i+1][j+1] =
        1. dp[i][j+1]        # * matches 0 element in s;
        2. dp[i][j]          # * matches 1 element in s;
        3. dp[i+1][j]        # * matches more than one in s.
    */
    bool isMatch(string s, string p) {
        int s_size = s.size();
        int p_size = p.size();
        if(s_size == 0){
            if(p.find_first_not_of('*') == string::npos){
                return true;
            }
            return false;
        }

        int not_star_cnt = 0;
        for(int i=0; i<p_size; i++){
            if(p[i] != '*'){
                not_star_cnt += 1;
            }
        }
        if(not_star_cnt > s_size){
            return false;
        }

        vector<vector<bool>> dp(p_size+1, vector<bool>(s_size+1, false));
        dp[0][0] = true;
        for(int i=0; i<p_size; i++){
            dp[i+1][0] = dp[i][0] && p[i] == '*';
        }

        for(int i=0; i<p_size; i++){
            for(int j=0; j<s_size; j++){
                if(p[i] == '*'){
                    dp[i+1][j+1] = dp[i][j] || dp[i][j+1] || dp[i+1][j];
                }
                else{
                    dp[i+1][j+1] = dp[i][j] && (p[i] == s[j] || p[i] == '?');
                }
            }
        }
        return dp[p_size][s_size];
    }
};

/*
"aa"
"a"
"aa"
"aa"
"aaa"
"aa"
"aa"
"*"
"aa"
"a*"
"ab"
"?*"
"aab"
"c*a*b"
*/
