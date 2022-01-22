#include <iostream>
#include <algorithm>
using namespace std;
/*
Let x = 1
Let calculation = (x*(x+1)) + (2 *(x + 1))
Let reversed_calc = reversed number of calculation [for example if calculation = 123, reversed_calc will be 321]
If reversed_calc can be divided by 4 without reminder then answer = answer + reversed_calc
Repeat all the calculations until you have x = 543
The final answer will be the flag when x = 543
*/

int main(){
    int calc, rev_calc, answer = 0;
    string str_num;
    for (int x = 1; x <= 543; x++){
        calc = (x+1)*(x+2);
        str_num = to_string(calc);
        reverse(str_num.begin(), str_num.end());
        rev_calc = stoi(str_num);

        if (rev_calc % 4 == 0)  answer += rev_calc;
    }
    cout << answer;
}