! #3 ln(x) WITH ERROR APPROXIMATION
! NAME : ANIK MANDAL - 21024001
! DATE : Feb 28, 2022
!__________________________________________________

program ln

implicit none

real :: x, n, er, eps, s, d
integer :: i

write(*,*) "Give your number..."
read(*,*) n
write(*,*) "Accuracy you want..."
read(*,*) eps

if (n > 1.0) then
	x = 1.0 - (1/n)
else
	x = 1.0 - n
end if

i = 1

er = 100.0
s = 0.0
d = 1000.0

do while (er > eps)
	s = s + (x**i)/i
	i = i + 1
	er = abs(s-d)
	d = s
end do

if (n > 1.0) then
	write(*,*) "Value of ln(",n,") :", s
else
	write(*,*) "Value of ln(",n,") :", -s
end if

end program ln
