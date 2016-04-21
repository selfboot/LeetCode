/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-21 11:29:55
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
    /*
    Two pointers: one go 1 step, another one go 2 steps every time.
    Then if the list has a cycle, fast one will meet the slow one absolutely.
    Prove as follows:
    1. If has a circle
        Assume there are m nodes that not in cycle, and then k nodes in cycle.
        And slow one now go m+i nodes, fast one go 2m + 2i nodes whitout doubt.
        So, slow one in the i's node of the circle, and fast one m+2i
        That's say, fast one goes m+i steps more than slow one.
        As the nodes keep going,
        i grows so (m + i) mode k == 0, then fast and slow meet here.
    2. If not:
        fast one will meet None node.

    And once fast and slow meet at node i, then let slow continue going.
    One node from head go at the same time.  We can prove these two nodes
    will meet at the begin node of cycle, prove as follows:

    Assume before the node from head and the slow node meet, they go x steps.
    Then (x-m) mode k = (x+i) mod k, the minest x will be m clearly.
    Just remember we have proved:  (m + i) mode k == 0 before.
    */
    ListNode *detectCycle(ListNode *head) {
        bool hasCycle=false;
        ListNode* fast = head;
        ListNode* slow = head;
        while(fast && fast->next){
            fast=fast->next->next;
            slow=slow->next;
            if(slow==fast){
                hasCycle=true;
                break;
            }
        }
        if(!hasCycle){
            return NULL;
        }
        slow = head;
        while(slow!=fast){
            slow=slow->next;
            fast=fast->next;
        }
        return slow;
    }
};
