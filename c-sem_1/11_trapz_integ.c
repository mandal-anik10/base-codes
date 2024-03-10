//DETERMINATION OF THE INTEGRATION OF A FUNCTION BY USING TRAPEZOIDAL METHOD

#include <stdio.h>
#include <math.h>

int main()
{
    printf("\tDETERMINATION OF INTEGRATION OF A FUNCTION\n\v");

    float a,b,p,h,fa,fb,fp,s,sum;
    int n,i;
    /* suppose, the function is,
    f(x)=x*x-6*x+10=0
    and we are going to integrate this from x=3.0 to x=10.0
    */
    a=3.0;
    b=10.0;
    n=100000;
    h=(b-a)/(n-1);
    s=0.0;
    fa=a*a-6*a+10;
    fb=b*b-6*b+10;
    
    for(i=1;i<n;i++)
    {
        p=a+i*h;
        fp=p*p-6*p+10;
        s=s+fp;
    }
    sum=h*(fa+fb+2*s)/2;
    
    printf("Integration of the function f(x),from x=%0.2f to x=%0.2f is %f \n",a,b,sum);
}