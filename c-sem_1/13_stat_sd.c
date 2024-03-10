//DETERMINATION OF THE STANDARD DEVIATION OF A SET OF NUMBERS

#include <stdio.h>
#include <math.h>

int main(void)
{
    printf("\tDETERMINATION OF STANDARD DEVIATION\v\n");
    
    float s,s2,m,m2,sd;
    float set[8]={2.2,2.8,2.3,2.9,2.4,3.1,2.7,2.5};
    int i,n;
    n=8;
    s=0.0;
    s2=0.0;
    printf("The set of number is\nset[%d]={",n);
    
    for(i=0;i<n;i++)
    {
        printf("%0.2f\t",set[i]);
        s=s+set[i];
        s2=s2+set[i]*set[i];
    }
    printf("}");
    m=s/n;
    m2=s2/n;
    sd=sqrt(m2-m);
    printf("\nThe standard deviation of the set of numbers is %f \n",sd);
}