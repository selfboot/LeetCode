/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-06-27 13:27:33
 */


class Solution {
public:
    int lengthOfLastWord(string s) {
        int len = 0, tail = s.size() - 1;
        while (tail >= 0 && s[tail] == ' ') tail--;
        while (tail >= 0 && s[tail] != ' ') {
            len++;
            tail--;
        }
        return len;
    }
};

/*
""
"are"
"we are teams"
"we are teams    "
*/
