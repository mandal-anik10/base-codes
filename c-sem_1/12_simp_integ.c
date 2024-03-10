//DETERMINATION OF THE INTEGRATION OF A FUNCTION BY USING SIMPSON'S 1/3 METHOD

#include <stdio.h>
#include <math.h>

int main()
{
    printf("\tDETERMINATION OF INTEGRATION OF A FUNCTION\n\v");
    
    float a,b,p,h,fa,fb,fp,s,sum;
    int n,i;
    /* suppose, the function is,
    f(x)=x*x+x+1=0
    and we are going to integrate this from x=1.0 to x=5.0
    */
    a=1.0;
    b=5.0;
    n=100000;
    h=(b-a)/(n-1);
    s=0.0;
    fa=a*a+a+1;
    fb=b*b+b+1;
    
    for(i=1;i<n;i++)
    {
        p=a+i*h;
        fp=p*p+p+1;
        
        if(i%2==1)
        {       
            s=s+4*fp;
        }
        else
        {
            s=s+2*fp;
        }
    }
    sum=h*(fa+fb+s)/3;
    printf("Integration of the function f(x),from x=%0.2f to x=%0.2f is %f \n",a,b,sum);
}