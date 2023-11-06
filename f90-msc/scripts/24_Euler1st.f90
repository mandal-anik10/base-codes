! #24 SOLVING 1st ORDER DIFFERENTIAL EQUATION USING EULER METHOD
! NAME : ANIK MANDAL - 21024001
! DATE : May 10, 2022
!__________________________________________________

program Euler1st
implicit none
real :: x0, y0, xf, er, eps, h, x, y, m, z
integer :: n, i

write(*,*) "Give the initial boundary condition..."
read(*,*) x0, y0

write(*,*) "your final point..."
read(*,*) xf

write(*,*) "Maximum order of error, you want in calculation..."
read(*,*) eps

n = 4
er = 1
z = 10000

do while (er > eps)
	open(unit = 1, file = "/home/anik/local-codes/f90-msc/data/Euler1stSolved.txt")
	
	x = x0
	y = y0
	h = abs(xf-x0)/(n-1)
	do i = 1, n
		write(1,*) x, y
		call diff_eq(x, y, m)
		x = x + h
		y = y + m * h
	end do
	close(1)
	er = abs(y-z)
	z = y
	n = 2 * n
end do

end program Euler1st

subroutine diff_eq(x, y, m)
implicit none
real :: x, y, m

m = (2 * x - x * x) * exp(-x)

end subroutine diff_eq
