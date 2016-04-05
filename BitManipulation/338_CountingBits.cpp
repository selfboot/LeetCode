/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-05 17:22:31
 */

class Solution {
public:
    /*
    f[i] = f[i / 2] + i % 2
    or
    f[i] = f[i&(i-1)] + 1, i&(i-1) drops the lowest set bit
    */
    vector<int> countBits(int num) {
        vector<int> ans(num+1, 0);
        for(int i=1;i<=num;i++){
            ans[i] = ans[i>>1] + (i&0x1);
            // ans[i] = ans[i&(i-1)] + 1;
        }
        return ans;
    }
};

/*
0
1
12
*/
