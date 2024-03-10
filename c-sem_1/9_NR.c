//DETERMINATION OF THE SQUARE ROOT OF A NUMBER BY USING NEWTON-RAPHSON METHOD

#include <stdio.h>
#include <math.h>

int main(void)
{
    printf("\tDETERMINATION OF SQUARE ROOT\n\v");

    float n,x0,x1,f,df;
    n=8.0;
    x1=5.0;
    
    do
    {
        x0=x1;
        f= x0*x0-n;
        df= 2.0*x0;
        x1 = x0-(f/df);
    }
    while(fabs(x1-x0)>=0.000001);
    
    printf("The root of %0.2f is %f \n",n,x1);
}