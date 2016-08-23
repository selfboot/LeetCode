/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-08-22 20:03:11
 */

class Solution {
public:
    /*
    As long as there is a price gap, we gain a profit.
    */
    int maxProfit(vector<int>& prices) {
        int max_profit = 0;
        for(int i=1; i<prices.size(); i++){
            int diff = prices[i] - prices[i-1];
            max_profit += (diff > 0 ? diff : 0);
        }
        return max_profit;
    }
};

/*
[]
[3,4,5,6,2,4]
[6,5,4,3,2,1]
[1,2,3,4,3,2,1,9,11,2,20]
*/
