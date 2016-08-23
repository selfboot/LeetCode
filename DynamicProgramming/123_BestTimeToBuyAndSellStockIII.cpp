/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-08-23 10:53:01
 */

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n==0){
            return 0;
        }
        vector<int> pre_profit(n,0);
        vector<int> post_profit(n,0);

        int min_buy = prices[0];
        for(int i=1;i<n;i++){
            min_buy = min(prices[i], min_buy);
            pre_profit[i] =  max(pre_profit[i-1], prices[i]-min_buy);
        }

        int max_sell = prices[n-1];
        for(int j=n-2;j>=0;j--){
            max_sell = max(prices[j], max_sell);
            post_profit[j] = max(post_profit[j+1], max_sell-prices[j]);
        }

        int max_profit = 0;
        for(int i=0; i<n;i++){
            max_profit = max(max_profit, pre_profit[i] + post_profit[i]);
        }
        return max_profit;
    }
};

class Solution_2 {
public:
    /*
    Assume we only have 0 money at first, Then
    sell_2: The maximum if we've just sold 2nd stock so far.
    buy_2: The maximum if we've just buy 2nd stock so far.
    sell_1: The maximum if we've just sold 1nd stock so far.
    buy_1: The maximum if we've just buy 1st stock so far.
    Refer to:
    https://discuss.leetcode.com/topic/5934/is-it-best-solution-with-o-n-o-1
    */
    int maxProfit(vector<int>& prices) {
        int buy_1 = INT_MIN, buy_2 = INT_MIN;
        int sell_1 = 0, sell_2 = 0;
        for(int p: prices){
            sell_2 = max(sell_2, p+buy_2);
            buy_2 = max(buy_2, sell_1-p);
            sell_1 = max(sell_1, p+buy_1);
            buy_1 = max(buy_1, -p);
        }
        return sell_2;
    }
};

/*
[]
[1,2]
[1,3,5]
[2,8,3,9]
[2,8,3,9,1,2]
[2,8,3,9,1,9]
[6,5,4,3,2,1]
*/
