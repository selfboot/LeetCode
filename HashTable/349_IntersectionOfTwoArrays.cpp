/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-02 10:30:33
 */

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> sets1(nums1.begin(), nums1.end());
        vector<int> ans;
        for(auto &n : nums2){
            if(sets1.count(n)){
                ans.push_back(n);
                sets1.erase(n);
            }
        }
        return ans;
    }
};

class Solution_2{
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        int i = 0, j=0;
        vector<int> ans;
        while(i < nums1.size() && j < nums2.size()){
            if(nums1[i] > nums2[j]){
                j++;
            }
            else if(nums1[i] < nums2[j]){
                i++;
            }
            else{
                if(ans.size()==0 || nums1[i] != ans[ans.size()-1]){
                    ans.push_back(nums1[i]);
                }
                i++;
                j++;
            }
        }
        return ans;
    }
};

/*
[]
[]
[-1]
[]
[1,2,2,2,10,5]
[1,3,4,5,9]
*/
