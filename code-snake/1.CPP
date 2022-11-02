#include<iostream>
using namespace std;

float s(float a[], int n){
    if(n==0){
        return 0;
    }
    float b = s(a, n-1);
    if(a[n-1]>0) b = b + a[n-1];
    return b;
}

int main(){
    int n = 21;
    int a[n] ={10 -1 9 0 2 8 7 5 6 20 15 80 112 -4 -3 -9 17 14 0 3 4};
    cout << s;
    return 0;
}