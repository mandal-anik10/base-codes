//DETERMINATION OF THE VALUE OF sinX

#include <stdio.h>
#include <math.h>

int main(void)
{
    printf ("\tTHE VALUE OF sinX\n\v");
    float x,a,t,sum;
    int i,n,z,f;
    
    x=30.0;
    a=4*atan(1)*x/180;
    sum=0.0;
    z=1;
    f=1;
    n=12;
    
    for(i=1;i<=12;i++)
    {
        f=f*i;
        if(i%2==1)
        {
            z=z+1;
            t=pow(a,i)*pow(-1,z)/f;
            printf("The %d no. term is %f\n",i,t);
            
            sum=sum+t;
        }
        f=1;
        t=0.0;
    }
    printf("\vThe value of sin(%0.2f) = %0.5f \n",x,sum);
}