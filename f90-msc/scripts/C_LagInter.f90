! #CLASSWORK: LAGRANGE INTERPOLATION
! NAME : ANIK MANDAL - 21024001
! DATE : May 2, 2022
!__________________________________________________

program Lagrange
implicit none

real :: s, p, x1, y1, x2, y2, y , h
integer :: i, j, k, n, np
real, allocatable, dimension(:) :: x_data, y_data, x

write(*,*) "Input the number of datas you have..."
read(*,*) n

write(*,*) "Input the number of point, where you want to get the value of the function..."
read(*,*) np

allocate(x_data(n))
allocate(y_data(n))
allocate(x(np))

open(unit = 1, file= "/home/anik/local-codes/f90-msc/data/Lagrange.txt")

do i = 1, n 
	read(1,*) x_data(i),y_data(i)
end do

h = abs(x_data(n) - x_data(1))/(np-1) 
do k = 1, np 
	x(k) = x_data(1) + (k-1) * h
end do

!write(*,*) "Input the points along x axis..."

!do k = 1, np
!	read(*,*) x(k)	
!end do

open(unit = 1, file = "/home/anik/local-codes/f90-msc/data/LagInterFit.txt")

do k = 1, np
	s = 0.0

	do i = 1, n
		p = 1.0
		do j = 1, n
			if (j .NE. i) then
				p = p * (x(k)-x_data(j))/(x_data(i)-x_data(j))
			end if
		end do
		s = s + p * y_data(i)
	end do

	y = s
	write(1,*) x(k), y
	write(*,*) "the value of the function at", x(k), ":", y 
end do

end program Lagrange 
