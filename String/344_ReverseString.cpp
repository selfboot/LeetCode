/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-04 14:03:42
 */

class Solution {
public:
    string reverseString(string s) {
        long low=0, high=s.size()-1;
        while(low < high){
            swap(s[low++], s[high--]);
        }
        return s;
    }
};

/*
""
"hello"
"  HELLO "
*/
