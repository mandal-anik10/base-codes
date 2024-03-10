//DETERMINATION OF THE VALUE OF π

#include <stdio.h>
#include <math.h>

int main(void)
{
    printf("\tTHE VALUE OF π\v\n");
    
    float a,b,c,d,x,y,t,t0,sum;
    int i,j,k,p,n,u,v;
    
    a=sqrt(8.0);    
    b=9801.0;
    i=0;
    n=5;
    u=1;
    v=-1;
    t0=(1*(1103+26390*0))/(1*1);
    /* as we know that,
    0! = 1
    so,
    (4*0)! = 1
    pow(0!,4) = 1
    and, we also know that,
    pow(396,4*0)= 1 */
    sum=t0;
    
    do
    {
        i=i+1;
        p=4*i;
        for(j=1;j<=p;j=j+1)
        {
            u=u*j;
        }
        for(k=1;k<=i;k=k+1)
        {
            v=v*k;
        }
        c=u*(1103+26390*i);
        d=pow(v,4)*pow(396,p);
        t=c/d;
        sum=sum+t;
    }
    while(i<=n);
    
    y=a*sum/b;
    x=1/y;

    printf("The value of π is %f \n",x);
}