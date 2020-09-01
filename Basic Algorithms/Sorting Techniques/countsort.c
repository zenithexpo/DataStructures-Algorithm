#include<stdlib.h>
#include<stdio.h>

int FindMax(int A[], int n){
	int max = 0;
	for(int i=0; i<n; i++){
	if(A[i]>max){
		max=A[i];
		}
	}return(max);
}

void count(int A[], int n){
	int i,j,k, *B;
	k = FindMax(A,n);
	B = (int *)malloc(sizeof(int)*k+1);
	for(i=0;i<k+1;i++)
	{B[i]=0;}
	for(i=0;i<n;i++)
	{  B[A[i]]++;}

	i=0,j=0;
	while(j<k+1)
	{
	 if(B[j]>0)
	{ A[i++] = j;
	  B[j]--;
	}
	else{ j++;}
	}


}





int main()
{
	int A[]={11,13,7,12,16,9,24,5,10,3}, n=10,i;
	count(A, n);
	for(i=0;i<n;i++)
	{printf("%d", A[i]);printf("\n");}
	


}