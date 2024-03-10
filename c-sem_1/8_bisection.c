//DETERMINATION OF SQUARE ROOT OF A NUMBER BY BISECTION METHOD

#include <stdio.h>
#include <math.h>

// function
float f(float x)
{
    return x*x-12;
}

int main(void)
{
    printf("\tDETERMINATION OF SQUARE ROOT\n\v");
    
    double error,a,b,c,d;
    a=1;
    b=5;
    error=0.000000000000001;
    
    do
    {
        c=(a+b)/2;
        d=f(c);
        if(d<0)
        {
            a=c;
        }
        else
        {
            b=c;
        }
    }
    while(fabs(b-a)>=error);

    printf("The value of square root is %f \n",c);
}