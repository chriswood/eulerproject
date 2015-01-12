// my second program in C++
#include <iostream>
#include <math.h>

using namespace std;

/*
 * Find divisors of a number, then sum them
 */
const int limit = 10000;

bool amicable(int, int[], int);

bool amicable(int a, int arr[], int index){
    int stop1 = ceil(float(a)/2.0);
    int stop2 = 0;
    int sum1 = 0;
    int sum2 = 0;

    for(int i=1; i<=stop1; i++){
        if(a%i == 0){
            sum1 += i;
        };
    }
    stop2 = ceil(float(sum1)/2.0);
    for(int i=1; i<=stop2; i++){
        if(sum1%i == 0){
            sum2 += i;
        };
    }
    if(sum2 == a && a != sum1){ //amicable pair
        arr[index] = a;
        return(true);
    }
    return(false);
}

int main(){
    int storage[limit];
    bool am;
    int index = 0;
    int total = 0;
    for(int i=4;i<limit;i++){
        am = amicable(i, storage, index);
        if(am){
            total += i;
            index++;
        }
        cout << i << "\n";
    }
    cout << "total: " << total << "\n";
    
    return(0);
}
