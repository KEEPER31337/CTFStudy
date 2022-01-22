#include <iostream>
using namespace std;

// problem code -> reverse the order

int main() {
	string flag = "0Un5Hfz02zQ=NtVB0=RZfMSX";

	for (int i = flag.length()-1; i >= 0; i--){
		for (int j = flag.length()-1; j > i; j--){
			char x = flag[j];
			flag[j] = flag[j-1];
			flag[j-1] = x;
		}
	}

	cout << flag << endl;

	return 0;
}
