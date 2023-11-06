! #1 BASIC STUFF: READ, WRITE AND IF-ELSE
! NAME : ANIK MANDAL - 21024001
! DATE : Fed 24, 2022
!__________________________________________________

program Run
implicit none

real :: x, y, eps
integer :: a, b

write(*,*) "Hello Universe! "

write(*,*) "Please give your two numbers and then two integer numbers..."		
read(*,*) x, y, a, b
write(*,*) "x = ", x, "y=", y, "a=", a, "b=", b

write(*,*) "Now give epsilon value for real numbers..."
write(*,*) "(Numerical resolution/limit of a real number to be considered as zero)"		
read(*,*) eps

if (b == 0) then
	write(*,*) "Oops! your b value can't be zero"
	
	if (abs(y) < eps) then
		write(*,*) "Oops again! your y value can't be zero"
	else
		write(*,*) "x/y=", x/y
	end if
	
else
	write(*,*) "a/b=", a/b
	
	if (abs(y) < eps) then
		write(*,*) "Oops! your y value can't be zero"
	else
		write(*,*) "x/y=", x/y
	end if
end if

end program Run
