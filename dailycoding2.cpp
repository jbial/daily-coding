#include<iostream>

using std::cout;
using std::endl;

int* productify(int arr[], int size) {
    int *products = new int[size];
    int left[size], right[size];

    left[0] = 1;
    right[size-1] = 1;

    for (int i = 1; i < size; i++) {
        left[i] = left[i-1]*arr[i-1];
    }
    for (int j = size-2; j > 0; j--) {
        right[j] = right[j+1]*arr[j+1];
    }

    for (int k = 0; k < size; k++) {
        products[k] = left[k]*right[k];
    }

    return products;

}

void printArr(int arr[], int size) {
    cout << "[ ";
    for (int i = 0; i < size; i++) {
        if (i == size - 1) cout << arr[i];
        else cout << arr[i] << ", ";
    } 
    cout << " ]" << endl;
}

int main() {

    int test1[5] = {1,2,3,4,5};
    int test2[3] = {3,2,1};

    int *result1 = productify(test1, 5);
    int *result2 = productify(test2, 3);

    cout << "Test Cases" << endl;
    printArr(test1, 5);
    printArr(result1, 5);
    cout << endl;
    printArr(test2, 3);
    printArr(result2, 3);

    return 0;
}