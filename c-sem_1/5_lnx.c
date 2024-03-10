//DETERMINATION OF THE VALUE OF lnX

#include <stdio.h>
#include <math.h>

int main(void)
{
    printf("\tTHE VALUE OF lnX\v\n");
    
    float x,y,a,t,sum;
    int i,n;

    x=5.0;
    y=1/x;
    a=y-1.0;
    sum=0.0;
    n=20;
    i=0;
    
    do
    {
        i=i+1;
        t=pow(a,i)*pow(-1,i+1)/i;
        printf("The %d no. term is %f\n",i,-t);

        sum=sum+t;
    }
    while(i<=n);
    
    printf("\nThe value of ln(%0.2f) is %f \n",x,-sum);
}