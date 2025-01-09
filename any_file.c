#include<stdlib.h>
#include<stdio.h>

int my_num(int a){
    return 2*a - 1;
}

int main(){
    printf("This is a C program\n");
    int a = 1;
    a = my_num(a);
    printf("%d",a);
    return 0;
}