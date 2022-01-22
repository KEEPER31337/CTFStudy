#include <iostream>
#include <cmath>
#include <algorithm>
#include <iomanip>
using namespace std;

/* 
Find the GCD of the following numbers 
and add up the all integers of that GCD and multiply with 1234.
Number 1: 21525625
Number 2: 30135875 
*/

int main(){
    int a = 30135875, b = 21525625, n = __gcd(a, b);
    string gcd_num = to_string(n);

    unsigned long long answer = 0;
    for (char _n : gcd_num){
        answer += _n - '0';
    }
    cout << answer * 1234;
}