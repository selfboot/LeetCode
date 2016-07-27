/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-27 10:42:26
 */

class Solution {
public:
    /*
    Once you can understand the solution space tree, you just get it.

    Refer to:
    https://discuss.leetcode.com/topic/24523/java-standard-backtrace-ac-solutoin-short-and-clear
    */
    vector<string> addOperators(string num, int target) {
        vector<string> ans;
        dfs_search(ans, "", num, target, 0, 0, 0);
        return ans;
    }

    void dfs_search(vector<string> &ans, string path, const string &num,
                    int target, int pos, long value, long pre_num){
        /*
        Put binary operator in pos, and then calculate the new value.

        @pre_num: when process *, we need to know the previous number.
        */
        if(pos == num.size()){
            if(value == target){
                ans.push_back(path);
            }
            return;
        }

        for(int i=1; i+pos<=num.size(); i++){
            string cur_str = num.substr(pos, i);
            // Digit can not begin with 0 (01, 00, 02 are not valid), except 0 itself.
            if(i>1 && cur_str[0] == '0')    break;
            long cur_d = stoll(cur_str);
            if(pos==0){
                dfs_search(ans, cur_str, num, target, pos+i, cur_d, cur_d);
            }
            // All three different binary operators: +, -, *
            else{
                dfs_search(ans, path+"+"+cur_str, num, target, pos+i, value+cur_d, cur_d);
                dfs_search(ans, path+"-"+cur_str, num, target, pos+i, value-cur_d, -cur_d);
                dfs_search(ans, path+"*"+cur_str, num, target, pos+i,
                           value-pre_num+pre_num*cur_d, cur_d*pre_num);
            }
        }
    }
};

/*
"000"
0
"123"
6
"232"
8
"1005"
5
"3456237490"
9191
*/
