//DETERMINATION OF THE VALUE OF e^x

#include <stdio.h>
#include <math.h>

int main(void)
{
    printf("\tTHE VALUE OF e^x\n\v");
    
    float x,sum,t;
    int i,n,f;
    
    x=1.0;
    sum=0.0;
    n=5;
    f=1;
    
    for(i=1;i<=n;i++)
    {
        f=f*i;
        t=pow(x,i)/f;
        printf("\nThe %d no. of term is %f",i,t);
        sum=sum+t;
    }
    printf("\n\vThe value of e^(%0.1f) = %f \n",x,sum+1);
}