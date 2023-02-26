#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LENGTH 2500

int main() {

    FILE *file;
    int calories[MAX_LENGTH];
    int calories_sum[MAX_LENGTH];
    int i, j, k, n;
    char buffer[10];
    int sum, max_sum, sum3;

    file = fopen("./puzzle-input.txt", "r");

    if (file == NULL) {
        printf("Error opening file\n");
        return 1;
    }

    i = 0;
    while (fgets(buffer, 10, file) != NULL) {
        if (strlen(buffer) == 1) {
            calories[i] = -1;
        } else {
            calories[i] = atoi(buffer);
        }

        i++;
    }

    n = i;
    j = 0;
    for (i = 0; i < n; i++) {
        if (calories[i] != -1) {
            sum = calories[i];
            for (k = i+1; k < n && calories[k] != -1; k++) {
                sum += calories[k];
            }
            calories_sum[j] = sum;
            j++;
            i = k - 1;
        }
    }

    max_sum = 0;
    for (i = 0; i < j; i++) {
        if (calories_sum[i] > max_sum) {
            max_sum = calories_sum[i];
        }
    }
    printf("%d\n", max_sum);

    sum3 = 0;
    for (i = 0; i < 3; i++) {
        max_sum = 0;
        for (k = 0; k < j; k++) {
            if (calories_sum[k] > max_sum) {
                max_sum = calories_sum[k];
            }
        }
        sum3 += max_sum;
        for (k = 0; k < j; k++) {
            if (calories_sum[k] == max_sum) {
                calories_sum[k] = -1;
            }
        }
    }
    printf("%d\n", sum3);

    fclose(file);
    return 0;
}
