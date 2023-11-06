! #5 MERGING OF TWO LIST
! NAME : ANIK MANDAL - 21024001
! DATE : Mar 5, 2022
!__________________________________________________

program array

implicit none

integer :: l, m, n, i, p
real, allocatable, dimension(:) :: A, B, C

write(*,*) "Give number of elements of A as l, of B as m..."
read(*,*) l, m
n = l + m
allocate(A(l))
allocate(B(m))
allocate(C(n))

write(*,*) "Type List A..."
do i = 1, l
	read(*,*) A(i)
end do

write(*,*) "Type List B..."
do i = 1, m 
	read(*,*) B(i)
end do

write(*,*) "List A : ", A
write(*,*) "List B : ", B

do i = 1, n
	if (i <= l) then
		C(i) = A(i)
	else
		p = i-l
		C(i) = B(p)
	end if
end do
	
write(*,*) "Marged List C : ", C


end program array
