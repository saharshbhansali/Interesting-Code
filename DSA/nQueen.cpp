// The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.

#include <iostream>
using namespace std;

bool isSafe(int **arr, int x, int y, int n){

    //column check
    for(int i=0;i<x;i++){
        if(arr[i][y]==1)
            return false;
    }

    //left diagonal check
    int row=x;
    int col=y;

    while(col>=0 && row>=0){
        if(arr[row][col]==1)
            return false;
        row--;
        col--;
    }

    //right diagonal check
    row=x;
    col=y;

    while(col<n && row>=0){
        if(arr[row][col]==1)
            return false;
        row--;
        col++;
    }

    return true;
}


bool placeQueen(int **arr, int x, int n){

    if(x>=n)
        return true;

    for(int col=0; col<n; col++){
        if(isSafe(arr,x,col,n)){

            arr[x][col]=1;
        
            if(placeQueen(arr,x+1,n))
                return true;
        }

        arr[x][col]=0; 
    }

    return false;
}


int main(){

    int n;
    cin>>n;
    int** arr= new int*[n];
    for(int i=0; i<n;i++){
        arr[i]=new int[n];
        for(int j=0; j<n; j++){
            arr[i][j]=0;
        }
    }

    if(placeQueen(arr,0,n)){
        for(int i=0; i<n; i++){
            for(int j=0; j<n;j++){
                cout<<arr[i][j]<<" ";
            }
            cout<<endl;
        }
    }


    return 0;
}