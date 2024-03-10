//DETERMINATION OF THE ROOTS AND NATURE OF ROOTS OF A QUADRATIC EQUATION

#include <stdio.h>
#include <math.h>

int main(void)
{
    printf("\tDETERMINATION OF ROOTS AND NATURE OF ROOTS\v\n");

    double a,b,c,d,r1,r2,r,i;
    /* if the equation is,
    x*x-6*x+10=0
    then,
    a= 1.0 , b= -6.0 , c= 10.0
    */
    a=1.0;
    b=-6.0;
    c=10.0;
    d=b*b-4*a*c;
    
    if(d>0.0)
    {
        printf("The roots are real and distinct");
        r1=(-1*b+sqrt(d))/(2*a);
        r2=(-1*b-sqrt(d))/(2*a);
        printf("\nThe roots are r1= %f and r2= %f \n",r1,r2);
    }
    else if(d==0.0)
    {
        printf("The roots are real and equal");
        r1=(-1*b+sqrt(d))/(2*a);
        r2=(-1*b-sqrt(d))/(2*a);
        printf("\nThe roots are r1= %f and r2= %f \n",r1,r2);
    }
    else
    {
        printf("The roots are complex");
        r=(-1*b)/2*a;
        i=(sqrt(fabs(d)))/(2*a);
        printf("\nThe roots are r1= %f+%fi and r2= %f-%fi \n",r,i,r,i);
    }
}