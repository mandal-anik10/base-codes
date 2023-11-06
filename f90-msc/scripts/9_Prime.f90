! #9 CHECK IF PRIME OR NOT
! NAME : ANIK MANDAL - 21024001
! DATE : Mar 10, 2022
!__________________________________________________

program prime

implicit none
integer :: n, i, root, m

write(*,*) "Give any number greater than 1..."
read (*,*) n

m =1

if (n == 2 .OR. n == 3) then
	write(*,*) n, "is a prime number"

else
	root = int(sqrt(float(n)))

	do i = 2, root 
		m = m * mod(n,i)
	end do

	if (m ==0) then
		write(*,*) n, " is not a prime number"
	else
		write(*,*) n, "is a prime number"
	end if
end if

end program prime
