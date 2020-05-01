#include<stdio.h>


int sqArr(void){

    int sqArr[100];
    for(int i = 0; i<100; i++){
        sqArr[i] = (i+1) * (i+1);
        printf("%d * %d = %d\n", i+1, i+1, sqArr[i]);
    }
    getch();
    return 0;
}

int fibArr(void){
    int fibArr[100] = {1, 1};
    printf("Fib(0) = 1\n");
    printf("Fib(1) = 1\n");
    for(int i = 2; i < 100; i++){
        fibArr[i] = fibArr[i-1] + fibArr[i-2];
        printf("Fib(%d) = %d\n", i, fibArr[i]);
    }
    getch();
    return 0;
}

int main(void){
    int x = 3, y = 7, z;
    z = 1>>x;
    printf("%d, %d, %d", x, y, z);

    getch();
    return 0;
}