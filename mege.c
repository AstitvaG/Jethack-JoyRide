[4:06 PM, 1/19/2020] Trusha: #include <stdlib.h>
#include <stdio.h>
#include <sys/time.h>

#define n 1000000
int A[n+1];


float tdiff(struct timeval *start,struct timeval *end)
{
	return (end->tv_sec - start->tv_sec)+1e-6*(end->tv_usec - start->tv_usec);
}
void merge(int arr[], int l, int m, int r) 
{ 
    int i, j, k; 
    int n1 = m - l + 1; 
    int n2 =  r - m; 
    int L[n1], R[n2]; 
    for (i = 0; i < n1; i++) 
        L[i] = arr[l + i]; 
    for (j = 0; j < n2; j++) 
        R[j] = arr[m + 1+ j]; 
    i = 0; 
    j = 0;  
    k = l; y 
    while (i < n1 && j < n2) 
    { 
        if (L[i] <= R[j]) 
        { 
            arr[k] = L[i]; 
            i++; 
        } 
        else
        { 
            arr[k] = R[j]; 
            j++; 
        } 
        k++; 
    } 
    while (i < n1) 
    { 
        arr[k] = L[i]; 
        i++; 
        k++; 
    } 
    while (j < n2) 
    { 
        arr[k] = R[j]; 
        j++; 
        k++; 
    } 
}
void mergeSort(int arr[], int l, int r) 
{ 
    if (l < r) 
    { 
        int m = l+(r-l)/2; 
        mergeSort(arr, l, m); 
        mergeSort(arr, m+1, r); 
  
        merge(arr, l, m, r); 
    } 
} 
int main(int argc,const char *argv[])
{
	for (int i = 0; i < n; ++i)
	{
			A[i] = (int)rand() /(int)RAND_MAX;
	}

	struct timeval start,end;
	gettimeofday(&start,NULL);

	mergeSort(A,0,n-1)

	gettimeofday(&end,NULL);
	printf("%0.6f\n", tdiff(&start,&end));
	return 0;
}