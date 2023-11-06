! #16 DETERMINING MOD(X, Y)
! NAME : ANIK MANDAL - 21024001
! DATE : Apr 12, 2022
!__________________________________________________

program modx
implicit none
integer :: x, y, c, i
real :: start, finish

write(*,*) "Input x"
read(*,*) x
write(*,*) "Input y"
read(*,*) y

call cpu_time(start)
i = 0
do
	if (x*i <= y .AND. y - x*i < x) then
		c = y - x*i
		write(*,*) "Value of", y, "Modulo", x,"=", c
		exit
	end if
	i = i + 1
end do                          

call cpu_time(finish)
write(*,*) "Execution time", finish-start,"s"

end program modx
