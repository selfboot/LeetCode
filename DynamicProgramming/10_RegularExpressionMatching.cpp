/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-07 22:22:45
 */


class Solution {
public:
    // Recursively
    bool isMatch(string s, string p) {
        if(p.empty())   return s.empty();
        if(p[1] == '*'){
            // x* matches empty string or at least one character: x* -> xx*
            return (isMatch(s, p.substr(2)) || !s.empty() && (s[0] == p[0] || '.' == p[0]) && isMatch(s.substr(1), p));
        }
        else{
            return !s.empty() && (s[0] == p[0] || '.' == p[0]) && isMatch(s.substr(1), p.substr(1));
        }
    }
};


class Solution_2 {
public:
    /*
    According to:
    https://leetcode.com/discuss/43860/9-lines-16ms-c-dp-solutions-with-explanations
    Dynamic Programming
        P[i][j] to be true if s[0..i) matches p[0..j) and false otherwise;
    */
    bool isMatch(string s, string p) {
        int m = s.length(), n = p.length();
        vector<vector<bool>> dp(m + 1, vector<bool> (n + 1, false));
        dp[0][0] = true;
        for (int i = 0; i <= m; i++)
            for (int j = 1; j <= n; j++)
                if (p[j - 1] == '*')
                    dp[i][j] = dp[i][j - 2] || (i > 0 && (s[i - 1] == p[j - 2] || p[j - 2] == '.') && dp[i - 1][j]);
                else dp[i][j] = i > 0 && dp[i - 1][j - 1] && (s[i - 1] == p[j - 1] || p[j - 1] == '.');
        return dp[m][n];

    }
};
