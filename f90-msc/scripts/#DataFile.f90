! #	CREATING DATA
! NAME : ANIK MANDAL - 21024001
! DATE : May 3, 2022
!__________________________________________________

program datafile
implicit none
integer :: i
real :: x, y, r, yl, yh, ye

open(unit=1, file="/home/anik/local-codes/f90-msc/data/LinearData.txt")
open(unit=2, file="/home/anik/local-codes/f90-msc/data/HyperData.txt")
open(unit=3, file="/home/anik/local-codes/f90-msc/data/ExpData.txt")

do i =1, 10
	call random_number(r)
	x = i
	
	yl = 3*x/2 + 7/5 + 3*(r-0.5)
	write(1,*) x, yl
	
	yh = 1/(3/4 + 2*(x +  (r-0.5)))
	write(2,*) x, yh
	
	ye = 0.5 * exp(0.6 * (x + (r-0.5)))
	write(3,*) x, ye
	
end do

end program datafile

