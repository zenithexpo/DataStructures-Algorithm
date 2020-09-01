#include<stdio.h>

//Iterative Merge sort , time complexity - O(nlogn) , space O(n)
//2 way merging
void Merge(int A[], int l, int mid, int h)
{
	int i=l,j=mid+1,k=l;
	int B[h+1];  //auxillary array
	i=k=l;
	j=mid+1;
	while(i<=mid & j<=h)
	{
	if(A[i]<A[j])
		B[k++]=A[i++];
	else
		B[k++]=A[j++];
	}
	for(;i<mid;i++) //copy rest of the elemenst if remaining.
		B[k++] = A[i];
	for(;j<h;j++)
		B[k++] = A[j];
	
	for(i=l;i<h;i++) // copy back to original array
		A[i]=B[i];
	
}

void MergeSort(int A[], int n)
{
	int i,p,l,mid,h;
	for(p=2;p<=n;p=p*2)  // number of pass, every time list will be doubled
	{
	  for(i=0;i+p-1<n; i=i+p) //2,4,8, so on
	  {
		l=i;
		h=i+p-1;
 		mid = (l+h)/2;
		Merge(A,l,mid,h);
	  }

	}

      if(p/2<n)  // remaining element if size is odd.
	Merge(A,0,p/2-1,n);


}

int main()
{
	int A[]={11,13,7,12,16,9,24,5,10,3}, n=10,i;
	MergeSort(A,n);
	for(i=0;i<n;i++)
	{printf("%d", A[i]);printf("\n");}
	


}