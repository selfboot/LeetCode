/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-09 14:38:26
 */

/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class NestedIterator {
public:
    /*
    According to:
    https://discuss.leetcode.com/topic/42042/simple-java-solution-using-a-stack-with-explanation

    In the constructor, we push all the nestedList into the stack from back to front,
    so when we pop the stack, it returns the very first element.
    Second, in the hasNext() function, we peek the first element in stack currently,
    and if it is an Integer, we will return true and pop the element.

    If it is a list, we will further flatten it.
    This is iterative version of flatting the nested list.
    Again, we need to iterate from the back to front of the list.
    */
    stack<NestedInteger> keep;
    NestedIterator(vector<NestedInteger> &nestedList) {
        for(auto it=nestedList.rbegin(); it!=nestedList.rend(); it++){
            keep.push(*it);
        }
    }

    int next() {
        int val = keep.top().getInteger();
        keep.pop();
        return val;
    }

    bool hasNext() {
        while(!keep.empty()){
            NestedInteger cur = keep.top();
            if(cur.isInteger()){
                return true;
            }
            keep.pop();
            vector<NestedInteger> new_list = cur.getList();
            for(auto it=new_list.rbegin(); it!=new_list.rend(); it++){
                keep.push(*it);
            }
        }
        return false;
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */

/*
[]
[1,[2,[3]]]
[[1,2],3,[4,5]]
[[[1,2,3], [4,5], 7], [8,9], 10]
*/
