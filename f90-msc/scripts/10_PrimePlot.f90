! #10 (r, theta) PLOT OF PRIME NUMBERS
! NAME : ANIK MANDAL - 21024001
! DATE : Mar 11, 2022
!__________________________________________________

Program Prime

implicit none
integer :: n, i, j, m, c, root
real :: x, y
integer, allocatable, dimension(:) :: num

write(*,*) "Max limit..."
read(*,*) n

allocate(num(0))

open(unit=1, file= "/home/anik/local-codes/f90-msc/data/Prime.txt")				! for storing prime numbers
open(unit=2, file= "/home/anik/local-codes/f90-msc/data/Prime_PlotData.txt")		! for storing x-y data for ploting

c = 1

! Storing prime in a txt file
do i = 1, n
	root = int(sqrt(float(i)))
	m = 1

	do j = 2, root 
		m = m * mod(i, j)
	end do

	if (m /= 0) then
		write(1,*) c, i 
		num = [num, i]
		c = c + 1
	end if
end do

! Creating (x,y) data for the series
do i = 1, size(num)
	x = num(i)*cos(float(num(i)))
	y = num(i)*sin(float(num(i)))
	write(2,*) x, y
end do

end Program Prime
