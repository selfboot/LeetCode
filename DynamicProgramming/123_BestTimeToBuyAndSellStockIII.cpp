/*
* @Author: xuelangZF
* @Date:   2016-03-09 14:10:44
* @Last Modified by:   xuelangZF
* @Last Modified time: 2016-03-09 14:10:44
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
