/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-06-30 15:29:11
 */

class Solution {
public:
    bool isNumber(string s) {
        /*
        DFA.  Details can be found here:
        https://github.com/xuelangZF/LeetCode/blob/master/Images/65_ValidNumber.png
        https://github.com/xuelangZF/LeetCode/blob/master/Images/65_StateConvert.png
        */
        //delete the  prefix whitespace
        while(s[0]==' ')  s.erase(0,1);
        //delete the suffix whitespace
        while(s[s.size()-1]==' ') s.erase(s.size()-1, 1);
        if(s.size() == 0){
            return false;
        }
        vector<vector<int>> DFA_states_convert = {
            {2, 1, 8, -1},
            {2, -1, 8, -1},
            {2, -1, 3, 5},
            {4, -1, -1, 5},
            {4, -1, -1, 5},
            {7, 6, -1, -1},
            {7, -1, -1, -1},
            {7, -1, -1, -1},
            {4, -1, -1, -1}
        };

        int state = 0;
        for(char c : s){
            int num = input_num(c);
            if(num==-1){
                return false;
            }
            state = DFA_states_convert[state][num];
            if(state==-1){
                return false;
            }
        }
        if(state == 2 || state == 3 || state == 4 || state ==7){
            return true;
        }
        return false;
    }

private:
    int input_num(char c){
        if(c>='0' && c<='9'){
            return 0;
        }
        else if(c=='+' || c=='-'){
            return 1;
        }
        else if(c=='.'){
            return 2;
        }
        else if(c=='e'){
            return 3;
        }
        else{
            return -1;
        }
    }
};

/*
# True
"""
" .1"
"012"
"+12"
"-12"
"12e1"
"12e-1"
"12e+1"
"12e0"
"0e1"
"-1e1"
"1.2"
".2"
".1e1"
"+.2"
"1."
"      .1 "
"46.e3"
"""

# False
"""
""
".e1"
"+.e3"
"10e1.2"
"+-12"
"12e"
"e1"
"1e1e1"
"0xaf"
"      .1 2"
"."
"  ."
" -."
*/
