#include <iostream>

using std::cout;
using std::endl;

struct Node {
    int val;
    Node *npx;
};

Node * XOR(Node *a, Node *b) {
    return (Node *) ((uintptr_t)(a) ^ (uintptr_t)(b));
}

void insert(Node **head, int data) {
    Node *new_node = new Node;
    new_node->val = data;
    new_node->npx = XOR(NULL, *head);

    if (*head) {
        Node *next = XOR((*head)->npx, NULL);
        (*head)->npx = XOR(new_node, next);
    }
    *head = new_node;
} 

void printList(Node *head) {
    Node *curr = head;
    Node *prev = NULL;
    Node *next;

    while (curr) {
        cout << curr->val << " ";
        next = XOR(prev, curr->npx);

        prev = curr;
        curr = next;
    }

}

int main() {

    Node *head = NULL;
    insert(&head, 1);
    insert(&head, 2);
    insert(&head, 3);
    insert(&head, 4);

    printList(head);

    return 0;
}