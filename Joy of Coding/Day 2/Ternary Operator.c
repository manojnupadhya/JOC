﻿#include <stdio.h>

int main()
{
    int a,x;
    x=(a>18)?a:18;
    printf("enter the age a of person\n");
    scanf("%d",&a);
    if (a>18)
    {
        printf("a is eligible for voting\n");
    }
    else
    {
        printf("a is not eligible for voting\n");
        printf("the eligibility for  voting is 18 years");
    }
Output 
enter the age  of person a
23
a is eligible for voting
enter the age  of person a
10
a is not eligible for voting 
