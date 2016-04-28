/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-28 11:19:51
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

 // Recursively
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1==NULL)    return l2;
        if(l2==NULL)    return l1;

        ListNode *head = NULL;
        if(l1->val <= l2->val){
            head = l1;
            head->next = mergeTwoLists(l1->next, l2);
        }
        else{
            head = l2;
            head->next = mergeTwoLists(l1, l2->next);
        }
        // head point to some node in l1 or l2, so can be returned here.
        return head;
    }
};

 // Iteratively
class Solution_2 {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *pre_head = new ListNode(0);
        ListNode *cur = pre_head;
        while(l1!=NULL && l2!=NULL){
            if(l1->val <= l2->val){
                cur->next = l1;
                l1 = l1->next;
            }
            else{
                cur->next = l2;
                l2 = l2->next;
            }
            cur = cur->next;
        }
        while(l1!=NULL){
            cur->next = l1;
            l1 = l1->next;
            cur = cur->next;
        }
        while(l2!=NULL){
            cur->next = l2;
            l2 = l2->next;
            cur = cur->next;
        }
        return pre_head->next;
    }
};

/*
[]
[]
[1,4,8,12]
[2,3]
[1,3,5,7,9]
[2,4,6,8,10]
*/
