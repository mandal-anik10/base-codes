! #7 SELECTION SORT
! NAME : ANIK MANDAL - 21024001
! DATE : Mar 7, 2022
!__________________________________________________

program Selection

implicit none

integer, allocatable, dimension(:) :: A
integer :: n, i, j, c

write(*,*) "Give number of elemets in list..."
read(*,*) n

allocate(A(n))

write(*,*) "Input your list..."
do i = 1, n 
	read(*,*) A(i)
end do

write(*,*) "So, the list is :", A

do i = 1, n-1
	do j = i + 1, n 
		if (A(i) > A(j)) then		! Ascending Order
			c = A(i)
			A(i) = A(j)
			A(j) = c
		end if
	write(*,*) A
	end do
end do

write(*,*) "Sorted list", A


end program Selection
