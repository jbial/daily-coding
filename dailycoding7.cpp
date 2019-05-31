#include <iostream>
#include <string>
#include <map>

using std::cout;
using std::endl;
using std::string;
using std::map;
using std::pair;
using std::stoi;

bool inMap(string s) {
    return stoi(s) < 27 && stoi(s) > 0;
}

int chartoi(char c) {
    return (int)c - 48;
}

int countDecodings(string enc, int len, map<int, int> &memo) {

    int result;
    int start = enc.length() - len;

    // Base cases
    if (chartoi(enc[start]) == 0) return 0;
    if (len == 0 || len == 1) return 1;

    // Memoization
    if (memo.find(len) != memo.end()) return memo[len];

    result = countDecodings(enc, len - 1, memo);
    if (len >= 2 && inMap(enc.substr(start, 2))) {
        result += countDecodings(enc, len - 2, memo);
    }
    memo.insert(pair<int,int>(len, result));
    return result;
}

int countDecodings(string enc) {
    map<int, int> memo;
    return countDecodings(enc, enc.length(), memo);
}

int main() {

    string tc1 = "";
    string tc2 = "3";
    string tc3 = "0";
    string tc4 = "111";
    string tc5 = "1234";
    string tc6 = "10101";
    string tc7 = "12345";
    string tc8 = "011111";
    string tc9 = "12131411";

    if (countDecodings(tc1) == 1 &&
        countDecodings(tc2) == 1 &&
        countDecodings(tc3) == 0 &&
        countDecodings(tc4) == 3 &&
        countDecodings(tc5) == 3 &&
        countDecodings(tc6) == 1 &&
        countDecodings(tc7) == 3 &&
        countDecodings(tc8) == 0) {
        cout << "Passed" << endl;
    } else {
        cout << "Failed" << endl;
    }

    return 0; 
}