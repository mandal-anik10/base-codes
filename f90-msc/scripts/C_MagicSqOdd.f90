! ## MAGIC SQUARE OF ODD NUMBER
! NAME : ANIK MANDAL - 21024001
! DATE : Apr 25, 2022
!__________________________________________________

program magic
implicit none
integer :: N, i, j, p, ni, nj, idx_i, idx_j
integer, allocatable, dimension(:,:) :: M

write(*,*) "Input your odd number..."
read(*,*) N

allocate(M(N,N))
M = M * 0

p = 1
i= 1
j = int((N+1)/2)

do while (p <= N*N)
	M(i,j) = p
	p = p + 1

	idx_i = i - 1 + N * N * N
	idx_j = j - 1 + N * N * N

	ni = mod((idx_i-1), N) + 1
	nj = mod((idx_j+1), N) + 1
	
	write(*,*) ni, nj
	if (M(i, j) /= 0) then
		i =  i + 1
	else
		i = ni
		j = nj
	end if
end do

end program magic
