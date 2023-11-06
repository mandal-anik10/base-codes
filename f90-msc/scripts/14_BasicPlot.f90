! #14 CREATING A DATA FILE AND PLOTING IT 
! NAME : ANIK MANDAL - 21024001
! DATE : Apr 11, 2022
!__________________________________________________

program Plot
implicit none
real :: c1, c2, v
integer :: i, n

write(*,*) "Input the number data points..."
read(*,*) n

open(unit=1, file="/home/anik/local-codes/f90-msc/data/IvsV.txt")
write(1,*) "# Voltage		Current1	Current2"

write(*,*) "input Voltage then corrasponding current value..."
do i = 1, n
	read(*,*) v, c1, c2
	write(1,*) v, c1, c2
end do
end program Plot

