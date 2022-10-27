#include<bits/stdc++.h>
using namespace std;
///////////////////
//code of insertion sort 
void insertionSort(int *input, int size){
    for(int i =0 ; i<size ; i++){
        int current = input[i];
        int j = i-1;
        while(input[j]>current && j>=0){
            input[j+1]=input[j];
            j--;
        }
        input[j+1]=current;
    }
    
}
/////////////////
 

int main()
{
	int t;
	cin >> t;
	
	while (t--)
	{
		int size;
		cin >> size;
		int *input = new int[size];

		for (int i = 0; i < size; i++)
		{
			cin >> input[i];
		}

		insertionSort(input, size);

		for (int i = 0; i < size; i++)
		{
			cout << input[i] << " ";
		}

		delete[] input;
		cout << endl;
	}

	return 0;
}