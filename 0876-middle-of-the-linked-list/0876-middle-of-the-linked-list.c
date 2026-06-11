/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    struct ListNode *temp;
    temp=head;
    while(head!=NULL && head->next!=NULL){
        head=head->next->next;
        temp=temp->next;
    }
    return temp;
}