/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-10 14:33:58
 */

class Solution {
public:
    /*
    Divide and Conquer inspired by find k-th number in sorted array.

    The complexity is of course O(log(M+N)).
    Similiar with the following answer except without slicing.
    https://discuss.leetcode.com/topic/6947/intuitive-python-o-log-m-n-solution-by-kth-smallest-in-the-two-sorted-arrays-252ms
    */
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int len1 = nums1.size();
        int len2 = nums2.size();
        int len = len1 + len2;
        if(len & 0x1 == 1){
            return find_kth(nums1, 0, len1, nums2, 0, len2, (len+1)/2);
        }
        else{
            return (find_kth(nums1, 0, len1, nums2, 0, len2, (len)/2) +
                    find_kth(nums1, 0, len1, nums2, 0, len2, (len)/2+1)) / 2.0;
        }
    }

    int find_kth(vector<int>& list1, int begin1, int end1,
                 vector<int>& list2, int begin2, int end2, int k){
        /*
        Find the kth number in two sorted list: list1 , list2

        Binary search as followers:
        Firstly cut list1 and list2 into two parts by t1 and t2, respectively.
            1. lis1_left ... list1[t1-th] ... list1_right,
            2. lis2_left ... list2[t2-th] ... list2_right
        Then compare value of list1[t1-th] and list2[t2-th] in list2.
        Three situations about the relation between list1[t1-th] and list2[t2-th]:
            1.  <  Equal the (k-t1)th number in list1_right and list_2 left.
            2.  >  Equal the (k-t2)th number in list1_left and list_2 right.
            3. ==  Find the k-th number.
        */
        int len1 = end1 - begin1;
        int len2 = end2 - begin2;
        if(len1 > len2){
            return find_kth(list2, begin2, end2, list1, begin1, end1, k);
        }
        if(len1 == 0){
            return list2[begin2+k-1];
        }
        if(k==1){
            return min(list1[begin1], list2[begin2]);
        }

        int t1 = min(k/2, len1);
        int t2 = k - t1;
        if(list1[begin1+t1-1] < list2[begin2+t2-1]){
            return find_kth(list1, begin1+t1, end1, list2, begin2, begin2+t2, k-t1);
        }
        else if(list1[begin1+t1-1] > list2[begin2+t2-1]){
            return find_kth(list1, begin1, begin1+t1, list2, begin2+t2, end2, k-t2);
        }
        else{
            return list1[begin1+t1-1];
        }
    }
};


/*
[]
[1]
[1,3]
[2]
[1]
[2,3,4,5,6]
[2,3,4]
[5,6,7]
*/


/*
Excellent explanation can be found here:
https://discuss.leetcode.com/topic/4996/share-my-o-log-min-m-n-solution-with-explanation

In statistics, the median is used for dividing a set into two equal length subsets,
that one subset is always greater than the other.

First let's cut A into two parts at a random position i:

      left_A             |        right_A
A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
Since A has m elements, so there are m+1 kinds of cutting( i = 0 ~ m ).
And we know: len(left_A) = i, len(right_A) = m - i .
Note: when i = 0 , left_A is empty, and when i = m , right_A is empty.

With the same way, cut B into two parts at a random position j:

      left_B             |        right_B
B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]

Put left_A and left_B into one set, and put right_A and right_B into another set.
Let's name them left_part and right_part :

      left_part          |        right_part
A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]

If we can ensure:

1) len(left_part) == len(right_part)
2) max(left_part) <= min(right_part)

then we divide all elements in {A, B} into two parts with equal length,
and one part is always greater than the other.
Then median = (max(left_part) + min(right_part))/2.

To ensure these two conditions, we just need to ensure:

(1) i + j == m - i + n - j (or: m - i + n - j + 1)
    if n >= m, we just need to set: i = 0 ~ m, j = (m + n + 1)/2 - i
(2) B[j-1] <= A[i] and A[i-1] <= B[j]
(For simplicity, I presume A[i-1],B[j-1],A[i],B[j] are
always valid even if i=0/i=m/j=0/j=n .
I will talk about how to deal with these edge values at last.)

So, all we need to do is:

Searching i in [0, m], to find an object `i` that:
    B[j-1] <= A[i] and A[i-1] <= B[j], ( where j = (m + n + 1)/2 - i )

When the object i is found, the median is:
    max(A[i-1], B[j-1]) (when m + n is odd)
    or (max(A[i-1], B[j-1]) + min(A[i], B[j]))/2 (when m + n is even)
*/
