! #8 INSERTION SORT
! NAME : ANIK MANDAL - 21024001
! DATE : Mar 7, 2022
!__________________________________________________

program Insertion

implicit none

integer, allocatable, dimension(:) :: A
integer :: n, i, j, k, c

write(*,*) "Give number of elemets in list..."
read(*,*) n

allocate(A(n))

write(*,*) "Input your list..."
do i = 1, n 
	read(*,*) A(i)
end do

write(*,*) "So, the list is :", A

do i = 2, n
	k = i
	do j = i-1, 1, -1 
		if (A(j) > A(k)) then			! Ascending Order
			c = A(k)
			A(k) = A(j)
			A(j) = c
			k = k - 1
		end if
	end do
	write(*,*) A
end do

write(*,*) "Sorted list", A

end program Insertion
