/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-09-06 20:40:19
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

class Solution {
public:
    ListNode * merge_list(ListNode *left, ListNode *right){
        ListNode *pre_head = new ListNode(0);
        ListNode *scan = pre_head;
        while (left && right){
            if (left->val <= right->val){
                scan->next = left;
                left = left->next;
            }
            else{
                scan->next = right;
                right = right->next;
            }
            scan = scan->next;
        }
        if(left != nullptr) scan->next = left;
        if(right != nullptr) scan->next = right;
        return pre_head->next;
    }

    ListNode* sortList(ListNode* head) {
        if(head == nullptr || head->next == nullptr){
            return head;
        }
        ListNode *slow=head, *fast=head, *pre_tail= nullptr;
        // Cut the list into two parts
        while (fast != nullptr and fast->next != nullptr){
            pre_tail = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        pre_tail->next = nullptr;

        ListNode *left = sortList(head);
        ListNode *right = sortList(slow);
        return merge_list(left, right);
    }
};

// QuickSort.  Time Limit Exceeded if using no trick.
// Refer to:
// https://discuss.leetcode.com/topic/15029/56ms-c-solutions-using-quicksort-with-explanations/2
class Solution_2 {
public:
    ListNode* partition(ListNode *begin, ListNode *end){
        if(begin == nullptr || begin->next == end){
            return begin;
        }
        ListNode *scan = begin->next;
        int pivot = begin->val;
        ListNode *pos = begin;
        while(scan != end){
            if(scan->val <= pivot){
                pos = pos->next;
                if(pos != scan){
                    swap(pos->val, scan->val);
                }
            }
            scan = scan->next;
        }
        swap(pos->val, begin->val);
        return pos;
    }

    ListNode* quicksort(ListNode* begin, ListNode* end){
        if(begin == end || begin->next == end){
            return begin;
        }
        ListNode *pos = partition(begin, end);
        ListNode* head = quicksort(begin, pos);
        quicksort(pos->next, end);
        return head;
    }

    ListNode* sortList(ListNode* head) {
        return quicksort(head, nullptr);
    }
};

/*
[]
[1]
[1,2]
[5,1,2]
[5,1,2,3]
[5,1,2,3,6,7,8,9,12,2]
*/
