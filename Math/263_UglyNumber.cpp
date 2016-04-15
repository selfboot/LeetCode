/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-15 22:23:06
 */

class Solution {
public:
    bool isUgly(int num) {
        int prime[] = {2,3,5};
        for(auto &n : prime){
            while(num!=0 && num%n==0)   num/=n;
        }
        return num==1;
    }
};

/*
-2147483648
1
0
14
8
*/
