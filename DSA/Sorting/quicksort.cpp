#include<bits/stdc++.h>
using namespace std;

int part(int input[],int st , int end){
    int pivote = input[end];
    int i = st-1;
     // cout<<st<<endl;
    for(int j =st ; j<= end ; j++){
        if(input[j]<pivote){
            i++;
            int temp = input[i];
            input[i] = input[j];
            input[j] = temp;
        }
    }
            int temp = input[i+1];
            input[i+1] = input[end];
            input[end] = temp;
    
    return i+1;
}
void quicksort1(int input[],int st , int end){
    if(st>=end){
        return ;
    }
    int pi = part(input , st , end);
    quicksort1(input,st ,  pi-1);
    quicksort1(input, pi+1 , end);
}
void quickSort(int input[], int size) {
  quicksort1(input,0 ,size-1);

}

int main(){
    int n;
    cin >> n;
  
    int *input = new int[n];
    
    for(int i = 0; i < n; i++) {
        cin >> input[i];
    }
    
    quickSort(input, n);
    for(int i = 0; i < n; i++) {
        cout << input[i] << " ";
    }
    
    delete [] input;

}
