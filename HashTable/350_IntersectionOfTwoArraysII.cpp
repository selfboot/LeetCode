/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-02 10:59:01
 */

class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        map<int, int> nums1_hash;
        for(auto &n : nums1){
            nums1_hash[n]++;
        }
        vector<int> ans;
        for(auto &n : nums2){
            if(nums1_hash.find(n) != nums1_hash.end() && nums1_hash[n]-- > 0){
                ans.push_back(n);
            }
        }
        return ans;
    }
};


class Solution_2{
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        int i=0, j=0;
        vector<int> ans;
        while(i<nums1.size() && j<nums2.size()){
            if(nums1[i] == nums2[j]){
                ans.push_back(nums1[i]);
                i++;
                j++;
            }
            else if(nums1[i] > nums2[j]){
                j++;
            }
            else{
                i++;
            }
        }
        return ans;
    }
};

/*
[]
[]
[1,2,2,2,3]
[3,2,2,2,3]
[1, 2, 2, 1]
[2, 2]
*/
