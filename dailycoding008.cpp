#include <iostream>

using std::cout;
using std::endl;

struct Node {
    int val;
    Node *left, *right;
};

Node* newNode(int val) {
    Node *temp = new Node;
    temp->val = val;
    temp->left = temp->right = NULL;
    return temp;
}

bool isUnival(Node *root, int &count) {

    if (root == NULL) return true;

    bool left = isUnival(root->left, count);
    bool right = isUnival(root->right, count);

    if (!left || !right) return false;

    if (root->left && root->val != root->left->val) {
        return false;
    }
    if (root->right && root->val != root->right->val) {
        return false;
    } 
    count++;
    return true;
}

int countUnivals(Node *root) {
    int count = 0; isUnival(root, count);
    return count;
}

int main() {

    Node *root1 = newNode(0);
    root1->left = newNode(1);
    root1->right = newNode(0);
    root1->right->left = newNode(1);
    root1->right->right = newNode(0); 
    root1->right->left->left = newNode(1);
    root1->right->left->right = newNode(1);

    Node *root2 = newNode(0);
    Node *temp = root2;
    for (int i = 0; i < 3; i++) {
        temp->right = newNode(0);
        temp = temp->right;
    }

    Node *root3 = newNode(0);
    root3->right = newNode(0);
    root3->right = newNode(1);

    Node *root4 = newNode(1);
    root4->left = newNode(1);
    root4->right = newNode(1);

    Node *root5 = newNode(1);
    root5->left = newNode(1);
    root5->right = newNode(1);
    root5->right->right = newNode(0);

    Node *root6 = newNode(0);
    root6->left = newNode(1);
    root6->left->left = newNode(1);
    root6->left->right = newNode(1);

    if (countUnivals(root1) == 5 &&
        countUnivals(root2) == 4 &&
        countUnivals(root3) == 1 &&
        countUnivals(root4) == 3 &&
        countUnivals(root5) == 2 &&
        countUnivals(root6) == 3) {
        cout << "Passed" << endl;
    } else {
        cout << "Failed" << endl;
    }

    return 0;
}