! #11 FIBONACCI SERIES
! NAME : ANIK MANDAL - 21024001
! DATE : Mar 11, 2022
!__________________________________________________

Program Fibonacci

implicit none
integer :: n, i, a, b, s
integer, allocatable, dimension(:) :: num

write(*,*) "Max limit..."
read(*,*) n

allocate(num(n))

a = 0
b = 1

num(1) = a
num(2) = b

! Storing Fibonacci series in a list
do i = 1, n-2
	s = a + b
	num(i+2) = s
	a = b
	b = s
end do

write(*,*) num

end Program Fibonacci