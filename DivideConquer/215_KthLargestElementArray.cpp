/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-08-30 09:42:07
 */

class Solution {
public:
    /*
    Algorithm using partition(looks like quicksort somehow).

    Firstly, initialize left to be 0 and right to be nums.size()
    Then we do a partition and retrive the pivot position.
    If position is equal with k, we have got the k-th element.
    Else if position is less than k, then the K-th element is in the right part.
    Else, the K-th element in the left part, and we can recursively solve it.
    */
    int partition(vector<int> &nums, int begin, int end) {
        int pivot = nums[begin];
        int pivot_index = begin;
        for(int i=begin+1; i!=end;i++){
            if(nums[i] >= pivot){
                pivot_index+=1;
                if(pivot_index != i){
                    swap(nums[i], nums[pivot_index]);
                }
            }
        }
        swap(nums[begin], nums[pivot_index]);
        return pivot_index;
    }

    int find_kth_number(vector<int> &arr, int k){
        int begin = 0, end = arr.size();
        assert(k>0 && k<=end);

        int target_num = 0;
        while (begin < end){
            int pos = partition(arr, begin, end);
            if(pos == k-1){
                target_num = arr[pos];
                break;
            }
            else if(pos > k-1){
                end = pos;
            }
            else{
                begin = pos + 1;
            }
        }
        return target_num;
    }
};


class Solution_2 {
public:
    /*
    Other possibility is to use a min heap that will store the K-th largest values.
    The algorithm iterates over the whole input and
    maintains the size of priority queue.
    */
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, std::greater<int>> min_heap;
        for(int n: nums){
            if(min_heap.size() < k) min_heap.push(n);
            else{
                if(n > min_heap.top()){
                    min_heap.pop();
                    min_heap.push(n);
                }
            }
        }
        return min_heap.top();
    }
};

/*
[1]
1
[3,2,1,5,6,4]
2
[1,2,1,3,9]
2
*/
