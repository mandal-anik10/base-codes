! #22 LEAST SQUARE HYPERBOLIC FIT
! NAME : ANIK MANDAL - 21024001
! DATE : May 3, 2022
!__________________________________________________

program LEAST
implicit none
real ::	sumx, sumyi, xb, yib, p1, p2, a1, a0, x, y, h
integer :: i, n
real, allocatable, dimension(:) ::  x_data, y_data

write(*,*) "Number of datas you have..."
read(*,*) n

allocate(x_data(n))
allocate(y_data(n))

open(unit=1, file="/home/anik/local-codes/f90-msc/data/HyperData.txt")

sumx = 0
sumyi = 0

do i = 1, n
	read(1,*) x_data(i), y_data(i)
	sumx = sumx + x_data(i)
	sumyi = sumyi + 1/y_data(i)
end do

xb = sumx/n
yib = sumyi/n

do i = 1, n
	p1 = p1 + (1/y_data(i) - yib)*(x_data(i) - xb)
	p2 = p2 + (x_data(i) - xb)*(x_data(i) - xb)
end do

a1 = p1/p2
a0 = yib - a1 * xb

write(*,*) "The Coefficients are : b=", a0, ", a=", a1		! y = 1/(ax + b)


h = abs(x_data(1)-x_data(n))/(10*n-1)
open(unit=2, file="/home/anik/local-codes/f90-msc/data/HyperFitData.txt")

do i = 0, 10*n-1
	x = x_data(1) + i * h
	y = 1/(a1 * x + a0)
	write(2,*) x, y
end do

end program LEAST

