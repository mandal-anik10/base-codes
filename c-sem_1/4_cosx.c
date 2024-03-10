//DETERMINATION OF THE VALUE OF cosX

#include <stdio.h>
#include <math.h>

int main(void)
{
    printf ("\tTHE VALUE OF cosX\n\v");

    float x,a,t,sum;
    int i,n,z,f;
    
    x=60.0;
    a=4*atan(1)*x/180;
    sum=1.0;
    n=7;
    z=0;
    f=1;
    i=1;
    
    do
    {
        i=i+1;
        f=f*i;
        if(i%2==0)
        {
            z=z+1;
            t=pow(a,i)*pow(-1,z)/f;
            printf("\nThe %d no. term is %f",i,t);
            
            sum=sum+t;
        }
    }
    while (i<=n);
    
    printf("\v\nThe value of cos(%0.2f) = %0.5f \n",x,sum);
}