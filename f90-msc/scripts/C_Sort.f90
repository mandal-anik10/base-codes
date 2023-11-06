! Classwork : Merging and sorting Already sorted lists
! Name : Anik Mandal - 21024001
! date : Mar 7, 2022
!__________________________________________________

program C_Sort

implicit none
integer, allocatable, dimension(:) :: C, D
integer :: A(5), B(5), i, j, k, p

A = [4, 7, 9, 13, 15]
B = [1, 2, 8, 16, 17]
p = 0
allocate(C(0))
allocate(D(10))

do i = 1, 5
	do j = p, 5
		if (A(i) > B(j)) then
			C = [C, B(j)]
			p = p + 1
		else
			C = [C, A(i)]
			exit
		end if
		
		if (j == 5 ) then
			do k = i,5
				C = [C, A(k)]
			end do
		end if
	end do
	if (i == 5 ) then
		do k = p, 5
			C = [C, B(k)]
		end do
	end if
	
end do
do i = 1, 10
	D(i) = C(i+1)
end do
write(*,*) "Sorted :", D

end program C_Sort
