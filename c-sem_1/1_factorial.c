//DETERMINATION OF FACTORIAL OF FIRST 20 NUMBERS

#include <stdio.h>
#include <math.h>

int main(void)
{
    printf("\tFACTORIAL OF FIRST 20 NUMBERS\n\v");
    
    double x;
    int i,n;
    
    n=20;
    x=1.0;
    
    for(i=1;i<=n;i++)
    {
        x=x*i;
        printf("\nThe factorial of %d is %0.3f",i,x);
    }
    printf("\n");
}
