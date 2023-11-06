! #6 BUBBLE SORT
! NAME : ANIK MANDAL - 21024001
! DATE : Mar 7, 2022
!__________________________________________________

program Bubble

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


do i = 1, n
	do j = 1, n-i+1
		if (A(j) > A(j+1)) then			! Ascending Order
			c = A(j)
			A(j) = A(j+1)
			A(j+1) = c
		end if
	end do
	write(*,*) A
end do

write(*,*) "Sorted list", A

end program Bubble
