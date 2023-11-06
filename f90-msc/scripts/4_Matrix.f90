! #4 MATRIX OPERATION : SUM, SUBTRACTION AND MULTIPLICATION
! NAME : ANIK MANDAL - 21024001
! DATE : Mar 5, 2022
!__________________________________________________

program Matrix

implicit none

integer, allocatable, dimension(:,:) :: A, B, Sp, Sm, C, D, M
integer :: i, j, k, ma, na, mb, nb, mc, nc, md, nd, s

! Defining Matrix A________________________
write(*,*) "Give the order of A as ma, na"
read(*,*) ma, na
allocate(A(ma, na))
write(*,*) "Input A matrix..."
do i = 1, ma
	do j = 1, na
		read(*,*) A(i,j)
	end do
end do
write(*,*) "Matrix A :", A

! Defining Matrix B________________________
write(*,*) "Give the order of B as mb, nb"
read(*,*) mb, nb
allocate(B(mb, nb))
write(*,*) "Input B matrix..."
do i = 1, mb
	do j = 1, nb
		read(*,*) B(i,j)
	end do
end do
write(*,*) "Matrix B :", B

! Matrix Addition and Subtraction________________________
if (ma==mb .AND. na==nb) then
	allocate(Sp(ma, na))
	allocate(Sm(ma, na))
	do i = 1, ma
		do j = 1, na
			Sp(i,j) = A(i,j) + B(i,j)
			Sm(i,J) = A(i,j) - B(i,j)
		end do
	end do
	
	write(*,*) "Addition of A and B : ", Sp
	write(*,*) "Subtraction of A and B : ", Sm
else
	write(*,*) "Order isn't matching!"
end if 	

!__________________________________________________

! Defining Matrix C________________________
write(*,*) "Give the order of C as mc, nc"
read(*,*) mc, nc
allocate(C(mc, nc))
write(*,*) "Input C matrix..."
do i = 1, mc
	do j = 1, nc
		read(*,*) C(i,j)
	end do
end do
write(*,*) "Matrix C :", C

! Defining Matrix D________________________
write(*,*) "Give the order of D as md, nd"
read(*,*) md, nd
allocate(D(md, nd))
write(*,*) "Input D matrix..."
do i = 1, md
	do j = 1, nd
		read(*,*) D(i,j)
	end do
end do
write(*,*) "Matrix D :", D

! Matrix Multiplication________________________
if (nc == md ) then
	allocate(M(mc,nd))
	do i = 1, mc
		do j = 1, nd
			s = 0
			do k = 1, nc
				s = s + C(i,k)*D(k,j)
			end do
			M(i,j) = s
		end do
	end do
	write(*,*) "Multiplication of C and D matrix : ", M
else
	write(*,*) "Invalid order for multiplication!"
end if

end program Matrix
