! #CLASSWORK: FINDING ROOT OF QUADRATIC EQUATION
! NAME : ANIK MANDAL - 21024001
! DATE : May 10, 2022
!__________________________________________________

program Eqn
implicit none
real :: a, b, c, p, q

write(*,*) "Input coefficients a, b, c..."
read(*,*) a, b, c
write(*,*) "So, your equ is..."
write(*,*) a,"* x^2 +", b, "* x +", c,"= 0"
write(*,*)

if (b*b > 4 * a * c) then
	write(*,*) "The roots are different and real..."
	p = -b/(2 * a)
	q = sqrt(b*b - 4 * a * c)/(2 * a)
	write(*,*) "The roots are: ", p-q, "and", p+q
else if (b*b < 4 * a * c) then
	write(*,*) "The roots are different and inaginary..."
	p = -b/(2 * a)
	q = sqrt(4 * a * c - b*b)/(2 * a)
	write(*,*) "The roots are: ", p, "-", q, "i", "and", p, "+", q, "i"
else
	write(*,*) "The roots are same and real..."
	p = -b/(2 * a)
	write(*,*) "The root is: ", p
end if

end program Eqn
