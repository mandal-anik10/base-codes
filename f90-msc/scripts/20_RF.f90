! #20 REGULA FALSI METHOD
! NAME : ANIK MANDAL - 21024001
! DATE : Apr 25, 2022
!__________________________________________________

program RF
implicit none

real :: x, x1, x2, f, f1, f2, eps, er

write(*,*) "Guess two solutions..."
read(*,*) x1, x2
write(*,*) "Maximum order of error, you want..."
read(*,*) eps

er = 1.0

do while (er > eps) 
	call func(x1, f1)
	call func(x2, f2)

	if (f1 * f2 < 0 ) then
		x = (x1 * f2 - x2 * f1) / (f2-f1)
		call func(x, f)
		
		if (f1 * f > 0) then
			er = abs(x - x1)
			x1 = x
		else if (f2 * f >  0) then
			er = abs(x - x2)
			x2 = x	
		else
			exit
		end if
	else 
		write(*,*) "Invalid Interval!"
		stop
	end if 
	
end do

write(*,*) "The value of root of the equation is ", x

end program RF

subroutine func(x, y)
implicit none
real :: x, y

y = x * x - 9.0 * x + 14.0		! Function to Integrate

end subroutine

