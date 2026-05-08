#include<stdio.h>
#include<time.h>
void swap(int* a, int* b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high)
{
    int p = arr[low];
    int i = low;
    int j = high;
    while(i<j)
    {
        while(arr[i] <= p && i<=high-1)
        {
            j--;
        }
        if(i<j){
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[low], &arr[j]);
    return j;
}

void quickSort(int arr[], int low, int high)
{
    if(low<high)
    {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi-1);
        quickSort(arr, pi+1, high);
    }
}

int main()
{
    int arr[] = {4,2,5,3,1};
    clock_t start, end;
    double cpu_time;
    int n = sizeof(arr)/ sizeof(arr[0]);
    start = clock();
    quickSort(arr, 0, n-1);
    end = clock();
    cpu_time = ((double) (end-start))/CLOCKS_PER_SEC;
    printf("%lf", cpu_time);
    for(int i=0; i<n; i++)
        printf("%d", arr[i]);
    return 0;
}
