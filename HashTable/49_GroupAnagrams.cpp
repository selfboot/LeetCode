/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-06-26 19:44:47
 */

class Solution {
public:
    /*
    According to: https://leetcode.com/discuss/51129/10-lines-76ms-easy-c-solution-updated-function-signature
    Write a count sort method and use it to sort the string.
    */
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> dict;
        for(auto str: strs){
            string sorted_str = countSort(str);
            dict[sorted_str].push_back(str);
        }

        vector<vector<string>> groups;
        for(auto group: dict){
            vector<string> g(group.second.begin(), group.second.end());
            groups.push_back(g);
        }
        return groups;
    }

private:
    string countSort(const string &str){
        int count[26] = {0};
        int len = str.length();
        for(auto c: str){
            count[c-'a'] += 1;
        }
        int p=0;
        string sorted_str = string(len, 'a');
        for(int i=0; i<26; i++){
            for(int j=0; j<count[i]; j++){
                sorted_str[p++] += i;
            }
        }
        return sorted_str;
    }
};


/*
[""]
["aaa", "aaa", "aa", "bb"]
["a", "b", "c", "d"]
*/
