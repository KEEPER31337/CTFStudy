#include <iostream>

using namespace std;
// problem : assembly code
// INT 21H - option
// AH : 2H --> print DL
// AH : 4CH --> exit 
// output : char(ascii) array 

int main(){
    char flag[] = {75,67,84,70,123,65,53,53,51,77,98,108,89,125};
    for (int i = 0; flag[i] != NULL; i++){
        cout << flag[i];
    }
}