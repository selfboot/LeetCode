/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-06-28 15:13:27
 */

class Solution {
public:
    string getPermutation(int n, int k) {
        vector<int> factorial(n, 1);
        for(int i=1; i<n; i++){
            factorial[i] = i * factorial[i-1];
        }
        vector<string> remain_array = {"1", "2", "3",
                                       "4", "5", "6", "7", "8", "9"};
        string ans = "";
        k -= 1;
        int pos = n;
        while(pos){
            int cur_pos = k / factorial[pos-1];
            string c = remain_array[cur_pos];
            remain_array.erase(remain_array.begin() + cur_pos);
            ans += c;
            k %= factorial[pos-1];
            pos -= 1;
        }
        return ans;
    }
};

/*
9
23
9
24
9
25
*/
