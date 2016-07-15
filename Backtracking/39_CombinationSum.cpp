/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-14 20:32:51
 */

class Solution {
public:
    /*
    Classic backtracking problem.

    One key point: for one specified number,
    just scan itself and numbers larger than it to avoid duplicate combinations.
    Besides, the current path need to be reset after dfs call in general.
    Refer to:
    https://discuss.leetcode.com/topic/23142/python-dfs-solution
    */
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        if(candidates.size() == 0){
            return {};
        }
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> ans;
        vector<int> path;
        dfs_search(candidates, 0, target, path, ans);
        return ans;
    }

    void dfs_search(vector<int>& candidates, int start, int target, vector<int> &path, vector<vector<int>> &ans){
        if(target==0){
            ans.push_back(path);
        }
        else{
            for(int i=start; i<candidates.size(); i++){
                if(candidates[i] > target){
                    return;
                }
                path.push_back(candidates[i]);
                dfs_search(candidates, i, target-candidates[i], path, ans);
                // Remember to do backtracking here.
                path.pop_back();
            }
        }
    }
};

/*
[]
2
[2, 3, 6, 7]
7
[1, 2, 3, 4]
10
*/
