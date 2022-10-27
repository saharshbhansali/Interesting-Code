#include <iostream>
using namespace std;
/////////
void merge(int input[], int st , int mid,int end){
    int *arr = new int[end-st+1];
    int i =st;
    int j = mid+1;
    int k =i;
    while(i<=mid && j<=end){
        if(input[i]<input[j]){
            arr[k] = input[i];
            i++;
            k++;
        }
        else{
            arr[k] = input[j];
            j++;
            k++;
            
        }
        
    }
    while(i<=mid){
            arr[k] = input[i];
            i++;
            k++;
        
        
    }
    while(j<=end){
            arr[k] = input[j];
            j++;
            k++;  
    }
    for(int i = st ; i<=end ; i++){
        input[i] = arr[i];
    }
    
    
}
void mergsort1(int input[], int st , int end){
    if(st>=end){
        return ;
    }
    int mid = (st+end)/2;
    mergsort1(input, st , mid);
    mergsort1(input, mid+1, end);
    merge(input, st, mid , end);
    
}
    
void mergeSort(int input[], int size){
      mergsort1(input, 0 , size-1);
}
//////////////////////


int main() {
  int length;
  cin >> length;
  int* input = new int[length];
  for(int i=0; i < length; i++)
    cin >> input[i];
  mergeSort(input, length);
  for(int i = 0; i < length; i++) {
    cout << input[i] << " ";
  }
}