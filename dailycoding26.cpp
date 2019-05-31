#include <iostream>

using std::cout;
using std::endl;

struct Node {
  int val;
  Node* next;
};


Node* removeKthFromEnd(Node* head, int k) {
  Node *fast, *slow;
  fast = slow = head;

  // Advance the fast pointer k times
  for (int i = 0; i < k + 1; i++) {
    // remove the first element if fast is null
    if (fast == NULL) return head->next;
    fast = fast->next;
  }

  // Advance both pointers in parallel until fast pts to NULL
  while (fast) {
    fast = fast->next;
    slow = slow->next;
  }
 
  // Remove the slow node
  slow->next = slow->next->next;

  return head;
}



//helper to print a linked list
void printList(Node* head) {
  while (head) {
    if (head->next) cout << head->val << "->";
    else cout << head->val;
    head = head->next;
  }
}



//add node to beginning of list
void listAdd(Node*& head, int data) {
  Node* node = new Node();
  node->val = data;
  node->next = head;
  head = node;
}



//helper function to make linked list from array
Node* makeList(int arr[], int size) {
  Node* head = NULL; 
  for (int i = size - 1; i >= 0; i--) {
    listAdd(head, arr[i]); 
  }
  return head; 
}


bool removeListTest(Node* head, int arr[], int size, int elem) {
  for (int i = 0; i < size && i != size - elem; i++) {
    if (head->val != arr[i]) return false;
    head = head->next;
  }
  return true;
}


int main() {

  int list[10] = {0,1,2,3,4,5,6,7,8,9};
  Node* head = makeList(list, 10); 

  if (
    removeListTest(head, list, 10, 1) &&    
    removeListTest(head, list, 10, 10) &&    
    removeListTest(head, list, 10, 9) &&    
    removeListTest(head, list, 10, 5)) {
    cout << "Passed" << endl;
  } else {
    cout << "Failed" << endl;
  }

  return 0;
}
