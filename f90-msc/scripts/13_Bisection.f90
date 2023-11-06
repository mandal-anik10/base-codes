! #13 BISECTION METHOD 
! NAME : ANIK MANDAL - 21024001
! DATE : Mar 11, 2022
!__________________________________________________

program Bisection
implicit none

real :: a, b, er, eps, c, d, f 

write(*,*) "Order of accuracy you want..."
read(*,*) eps

d = -9.0			! Any value to make evaluate error for the first time
er = 1.0

write(*,*) "Give two number(min and max) as interval..."

do
	read(*,*) a, b
	
	if ( f(a) * f(b) > 0.0 ) then
		write(*,*) "Invalid interval, give another two number"
		stop
	
	else
		do while (er >  eps)
			c = (a+b)/2.0
		
			if ( f(a) * f(c) < 0.0 ) then
				b = c
			elseif ( f(b) * f(c) < 0.0 ) then
				a = c
			else
				exit	! Exit way if both above conditions are false	
			end if
	
			er = abs(c-d)
			d = c
		end do
		
		exit			! Exit way from the infinite loop after reaching accuracy
		
	end if
end do

write(*,*) "The value of root of the equation is ", c

end program Bisection

function f(x)			! Defining function
implicit none
real :: x, f

f = x*x*x - 3*x*x - 3

end function f
