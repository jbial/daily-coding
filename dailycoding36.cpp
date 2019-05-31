/*
 * This problem was asked by Dropbox.
 *
 * Given the root to a binary search tree, 
 * find the second largest node in the tree.
 *
 * solution:
 *
 * Split the problem into two cases, the root has a right child, and
 * the root does not have a right child. 
 *  case1) Right child exists. In this case, travel down the right path
 *         only since the root is a BST, storing the parent along the way.
 *         then return the parent.
 *  case2) Right child does not exist. In this case, travel down the right
 *         starting from the root's left node, but this time, simply return
 *         the rightmost leaf from this process.
 * Runs in O(h) time where h is the height of the tree, constant space.
 */


#include <iostream>
#include <map>

using std::map;
using std::cout;
using std::endl;

struct Node {
  int val;
  Node *left, *right;
};


Node* newNode(int val) {
  Node* node = new Node;
  node->val = val;
  node->left = node->right = NULL;
  return node;
}


class Solution {

  public:

  Node* findLargestOrParent(Node* node, bool returnParent) {
    Node* parent = NULL;
    while (node->right) {
      parent = node;
      node = node->right;
    }
    return (returnParent)?parent:node;
  }

  Node* findSecondLargest(Node* root) {
    if (root == NULL)
      return NULL;
    if (root->left == NULL && root->right == NULL)
      return root;
    
    Node* second;
    if (root->left && root->right == NULL) 
      second = findLargestOrParent(root->left, false);
    else
      second = findLargestOrParent(root->right, true);
    return second;
  }

  bool testHandle(map<Node*, int> tests) {
    map<Node*, int>::iterator it;
    bool result = true;
    for (it = tests.begin(); it != tests.end(); it++) {
      result &= (findSecondLargest(it->first)->val == it->second);
    }
    return result;
  } 
};


int main() {

  map<Node*, int> tests;
  Solution sol;

  Node* root1 = newNode(5);
  tests[root1] = 5;

  Node* root2 = newNode(6);
  root2->left = newNode(4);
  root2->left->left = newNode(2);
  tests[root2] = 4;

  Node* root3 = newNode(6);
  root3->left = newNode(3);
  root3->left->right = newNode(4);
  tests[root3] = 4;

  Node* root4 = newNode(3);
  root4->right = newNode(4);
  root4->right->right = newNode(5);
  tests[root4] = 4;

  Node* root5 = newNode(3);
  root5->right = newNode(6);
  root5->right->left = newNode(4);
  root5->right->right = newNode(7);
  tests[root5] = 6;

  Node* root6 = newNode(1);
  root6->right = newNode(2);
  root6->right->right = newNode(3);
  root6->right->right->right = newNode(4);
  root6->right->right->right->right = newNode(5);
  tests[root6] = 4;

  if (sol.testHandle(tests))
    cout << "Passed" << endl;
  else
    cout << "Failed" << endl;


  return 0;
}
