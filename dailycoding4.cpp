#include <iostream>

using std::cout;
using std::endl;

int firstMissing(int arr[], int size) {
    int firstMissingNum = 1;
    for (int i = 0; i < size; i++) {
        if (arr[i] == firstMissingNum) firstMissingNum++;
    }
    return firstMissingNum;
}

int main() {

    int t1_arr[6] = {0, 0, 0, 0, 0, 0};
    int t2_arr[6] = {-1, 0, 2, 4, 3, 5};
    int t3_arr[4] = {3, 4, -1, 1};
    int t4_arr[5] = {6, -2, 3, 0};
    int t5_arr[3] = {1, 2, 0};
    int t6_arr[6] = {3,6,4,1,3,0};
    int t7_arr[6] = {1,1,1,1,1,1};

    if (firstMissing(t1_arr, 6)==1 &&
        firstMissing(t2_arr, 6)==1 &&
        firstMissing(t3_arr, 4)==2 &&
        firstMissing(t4_arr, 5)==1 &&
        firstMissing(t5_arr, 3)==3 &&
        firstMissing(t6_arr, 6)==2 &&
        firstMissing(t7_arr, 6)==2) {
        cout << "Passed" << endl;
    } else {
        cout << "Failed" << endl;
    }

    return 0;
}