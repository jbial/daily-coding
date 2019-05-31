#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;

struct Node {
    string val;
    struct Node *left, *right;
};

Node* newNode(string val) {
    Node* temp = new Node;
    temp->val = val;
    temp->left = temp->right = NULL;
    return temp;
}

string serialize(Node *root) {
    if (root == NULL) {
        return "NULL"; 
    }
    return root->val + "," + serialize(root->left) + "," + serialize(root->right);
}

Node* deserialize_rec(string &tree) {
        string &treecpy = tree;
        int pos = treecpy.find(",");
        string val = treecpy.substr(0, pos);
        treecpy = treecpy.substr(pos+1, treecpy.length()-1);

        if (val == "NULL") return NULL;

        Node *ret = newNode(val);

        ret->left = deserialize_rec(treecpy);
        ret->right = deserialize_rec(treecpy);

        return ret;
}

Node* deserialize(string tree) {
    string treecpy = tree;
    return deserialize_rec(treecpy);
}

int main() {

    Node *root = newNode("root");
    root->left = newNode("left");
    root->right = newNode("right");
    root->left->left = newNode("left.left");

    string serialized = serialize(root);
    string encdec = serialize(deserialize(serialized));

    if (serialized == serialize(deserialize(serialized))) {
        cout << "Passed" << endl;
    } else {
        cout << "Failed" << endl;
    }

    return 0;
}