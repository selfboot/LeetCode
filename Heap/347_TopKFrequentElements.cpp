/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-09 10:20:41
 */

class Solution {
private:
    struct bigger{
        bool operator()(pair<int, int> &one, pair<int, int>two){
            return one.second > two.second;
        }
    };
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        /* Use unordered_map and priority_queue(minheap) solution.
         *
         * Use unordered_map to avoid red-black hash implement, which takes almost O(n*lgn).
         * We build a min heap with size k, so the time complexity is O(nlgk).
         */
        unordered_map<int, int> num_count;
        for(const auto &n: nums){
            num_count[n] += 1;
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>, bigger> frequent_heap;
        // Build the min-heap with size k.
        for(auto it = num_count.begin(); it != num_count.end(); it++){
            if(frequent_heap.size() < k){
                frequent_heap.push(*it);
            }
            else if(it->second >= frequent_heap.top().second){
                frequent_heap.pop();
                frequent_heap.push(*it);
            }
        }

        vector<int> ans;
        while(!frequent_heap.empty()){
            auto top = frequent_heap.top();
            frequent_heap.pop();
            ans.push_back(top.first);
        }
        return ans;
    }
};


class Solution_2 {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        /* Using stl heap tool.
         * According to:
         * https://discuss.leetcode.com/topic/46664/36ms-neat-c-solution-using-stl-heap-tool
         */
        if (nums.empty()) return {};
        unordered_map<int, int> m;
        for (auto &n : nums) m[n]++;

        vector<pair<int, int>> heap;
        for (auto &i : m) heap.push_back({i.second, i.first});

        vector<int> result;
        make_heap(heap.begin(), heap.end());
        while (k--) {
            result.push_back(heap.front().second);
            pop_heap(heap.begin(), heap.end());
            heap.pop_back();
        }
        return result;
    }
};

/*
[1,1,1,2,2,3]
2
[1,1,2,3,3,3,4,4,4,4,1,1,1]
3
*/
