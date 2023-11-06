! #21 LEAST SQUARE LINEAR FIT
! NAME : ANIK MANDAL - 21024001
! DATE : May 3, 2022
!__________________________________________________

program LEAST
implicit none
real ::	sumx, sumy, xb, yb, p1, p2, a1, a0, x, y, h
integer :: i, n
real, allocatable, dimension(:) ::  x_data, y_data

write(*,*) "Number of datas you have..."
read(*,*) n

allocate(x_data(n))
allocate(y_data(n))

open(unit=1, file="/home/anik/local-codes/f90-msc/data/LinearData.txt")

sumx = 0
sumy = 0

do i = 1, n
	read(1,*) x_data(i), y_data(i)
	sumx = sumx + x_data(i)
	sumy = sumy + y_data(i)
end do

xb = sumx/n
yb = sumy/n

do i = 1, n
	p1 = p1 + (y_data(i) - yb)*(x_data(i) - xb)
	p2 = p2 + (x_data(i) - xb)*(x_data(i) - xb)
end do

a1 = p1/p2
a0 = yb - a1 * xb

write(*,*) "The Coefficients are : c=", a0, ", m=", a1  		! y = m*x + c

h = abs(x_data(1)-x_data(n))/(10*n-1)
open(unit=2, file="/home/anik/local-codes/f90-msc/data/LinearFitData.txt")

do i = 0, 10*n-1
	x = x_data(1) + i * h
	y = a1 * x + a0
	write(2,*) x, y
end do

end program LEAST

