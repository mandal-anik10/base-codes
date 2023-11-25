
# DETERMINATION OF THE VALUE OF π USING RAMANUJAN'S π SERIES


print("\tDETERMINATION OF THE VALUE OF π USING RAMANUJAN'S π SERIES\n")

s0 = (8**0.5)/9801 				# constant
(f1, f2, j, k) = (1, 1, 0, 0)

t1 = int(input("please, enter the maximum number of terms, you want for the approximation :"))

t0 = (1*(1103+26390*0))/(1*1)		# 1st term of the summation

print("\nThe value of π for 1 number of term	:", 1/(t0*s0))
# as we know that,
# 	0! = 1
# so,
#    (4 * 0)! = 1
#     pow(0!,4) = 1
# and, we also know that,
# 	pow(396,4*0)= 1
sum = t0

for t in range(1,t1):
    for i in range(0,t):
        i=i+1
        p=4*i
	
        while (j <= p):
            j=j+1
            f1=f1*j

        s1 = f1	                        # 1st part of every term of the summation
        s2 = 1103 + 26390*i	    		# 2nd part of every term of the summation
	
        while (k<=i):
            k=k+1
            f2=f2*k
		
        s3=f2**4                        # 3rd part of every term of the summation
        s4=396**p	      			    # 4th part of every term of the summation
	
        s = (s1*s2)/(s3*s4)           	# every term of the summation
        sum = sum+s                     # summation part
	
    pi=1/(s0*sum)
    print("The value of π for",t+1,"numbers of terms  :",pi)
    f1=1
    f2=1
    sum=t0
		

print("\nUltimate Approximated value of π upto",t+1,"terms :",pi)