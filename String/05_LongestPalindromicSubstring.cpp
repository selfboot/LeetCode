/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-04 21:41:17
 */

class Solution {
public:
    string longestPalindrome(string s) {
        if(s=="")   return "";
        else if(s.size() == 1) return s;
        int s_len = s.size();
        int max_begin=0, max_end=0;
        int pos = 0;
        while(pos < s_len){
            // No need to check the remainming, pruning here
            if(max_end-max_begin >= (s_len-pos) * 2 - 1){
                break;
            }
            int left = pos, right = pos+1;
            while(right < s_len && s[right] == s[right-1]){
                right ++;
            }
            pos = right;
            while(left-1>=0 && right<s_len && s[left-1]==s[right]){
                left -= 1;
                right += 1;
            }
            if(right - left > max_end - max_begin){
                max_begin = left;
                max_end = right;
            }
        }
        return s.substr(max_begin, max_end-max_begin);
    }
};

/*
""
"a"
"aa"
"dcc"
"aaaa"
"cccd"
"ccccdc"
"abcdefead"
*/
