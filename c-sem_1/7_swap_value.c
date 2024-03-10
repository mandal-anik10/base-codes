//SWAPPING OF VALUES OF TWO VARIABLES

#include <stdio.h>
#include <math.h>
    
int main(void)
{
    printf("\tSWAPPING OF VALUES OF TWO VARIABLES\v");
    
    int x,y;
    
    x=3;
    y=8;
    
    printf("\nAt first, x= %d and y= %d\n",x,y);
    
    x=x+y;
    y=x-y;
    
    x=x-y;
    
    printf("\nAfter swapping: x= %d and y= %d \n",x,y);
}