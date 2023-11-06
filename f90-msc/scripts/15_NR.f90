! #15 NEWTON-RAPHSON METHOD
! NAME : ANIK MANDAL - 21024001
! DATE : Apr 11, 2022
!__________________________________________________

program NR
implicit none
real ::  x, p, f, fp, er, eps

write(*,*) "Guess a solution..."
read(*,*) x

write(*,*) "Now give epsilon value for real numbers..."
write(*,*) "(Numerical resolution/limit of a real number to be considered as zero)"		
read(*,*) eps

er = eps + 1.0

do while (er > eps)
	call func(x, f, fp)

	if (abs(fp) > eps) then		! To avoid divide by zero error
		p = x
		x = p - f/fp
		er = abs(x-p)
	else
		write(*,*) "Invalid guess!"
		stop
	end if
end do 

write(*,*) "The value of root of the equation is ", x

end program NR

SUBROUTINE func(x, f, fp)
implicit none
real, intent(in) :: x
real, intent(out) :: f, fp

f = x * x * x - 3.0 * x * x + 3.0
fp = 3.0 * x * x - 6.0 * x 
 
return
end
