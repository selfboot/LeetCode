/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-06 21:22:30
 */

class Solution {
public:
    int strStr(string haystack, string needle) {
        if(needle=="")  return 0;
        int str_len = haystack.size();
        int pat_len = needle.size();
        for(int i=0;i<str_len-pat_len+1;i++){
            int j=0;
            for(;j<pat_len;j++){
                if(haystack[i+j] != needle[j]){
                    break;
                }
            }
            if(j == pat_len){
                return i;
            }
        }
        return -1;
    }
};

/*
""
""
"abaa"
"aa"
"aaabbb"
"abbb"
*/
