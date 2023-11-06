! #19 SECANT METHOD
! NAME : ANIK MANDAL - 21024001
! DATE : Apr 25, 2022
!__________________________________________________

program secant
implicit none
real ::  x0, x1, x, f0, f1, er, eps

write(*,*) "Guess two solutions..."
read(*,*) x0, x1
write(*,*) "Order of accuracy, you want..."
read(*,*) eps

er = 1.0

do while (er > eps)
	call func(x0, f0)
	call func(x1, f1)
	if (abs(f0-f1) > eps) then
		x = x1 - f1*(x1-x0)/(f1-f0)
		x0 = x1
		x1 = x
		er = abs(x1-x0)
	else
		write(*,*) "Invalid guess!"
		stop
	end if
end do 

write(*,*) "The value of root of the equation is ", x

end program secant

SUBROUTINE func(x, f)
implicit none
real, intent(in) :: x
real, intent(out) :: f

f = x * x * x - 3.0 * x * x + 3.0
 
return
end

