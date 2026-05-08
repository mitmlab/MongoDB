#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void selectionSort(int arr[], int n)
{
    int i, j, min, temp;

    for (i = 0; i < n - 1; i++)
    {
        min = i;
        for (j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[min])
                min = j;
        }

        if (min != i)
        {
            temp = arr[i];
            arr[i] = arr[min];
            arr[min] = temp;
        }
    }
}

int main()
{
    int arr[10000];
    int n, i, j;

    srand(time(0));

    for (i = 0; i < 1000; i += 100)
    {
        n = 5000 + i;

        for (j = 0; j < n; j++)
        {
            arr[j] = rand();
        }

        clock_t start, end;
        double cpu_time_used;

        start = clock();
        selectionSort(arr, n);
        end = clock();

        cpu_time_used = ((double)(end - start)) / CLOCKS_PER_SEC;

        printf("n = %d, time = %lf seconds\n", n, cpu_time_used);
    }

    return 0;
}
