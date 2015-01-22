#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;

void Sieve(int maxNum); //declaring a function

int main() {
	high_resolution_clock::time_point t1 = high_resolution_clock::now();
	Sieve(1000000);
	high_resolution_clock::time_point t2 = high_resolution_clock::now();

	/* Calculating function duration */
	auto duration = std::chrono::duration_cast<std::chrono::microseconds>( t2 - t1 ).count();

	cout << duration;
	return 0;
}

/* Standard for loop and Sieve primenumber algorithm*/
void Sieve(int maxNum) {
    int i, j;
    char *Data;

    Data = (char *) malloc(maxNum + 1);
    memset(Data, 1, maxNum+1);

    for (i=2; i<=maxNum; i++) {
        if (Data[i]) {
            for (j=i+i; j<=maxNum; j+=i) {
                Data[j]=0;
            }
        }
    }

    free(Data);
}
