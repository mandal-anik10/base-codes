! #13 TRAPEZOIDAL METHOD OF INTEGRATION WITH ERROR APPROXIMATION
! NAME : ANIK MANDAL - 21024001
! DATE : Apr 12, 2022
!__________________________________________________

program integrate
implicit none
integer :: i, n
real :: xi, xf, h, yi, xn, yn, s, d, er, eps
real, allocatable, dimension(:) :: xx, yy 

write(*,*) "Give limit of integration as xi, xf..."
read(*,*) xi, xf
write(*,*) "Order of accuracy, you want..."
read(*,*) eps

allocate(xx(0))
allocate(yy(0))
n = 3
d = 1000.0
er = eps + 1.0

do while (er > eps)
	xx = [xi]
	call f(xi,yi)
	yy = [yi]
	
	h = abs(xf-xi)/(n-1)
	
	do i = 1, n-1
		xn = i * h + xi
		call f(xn,yn)
		xx = [xx, xn]
		yy = [yy, yn]
	end do
	
	s = 0.0
	
	do i = 2, n-1
		s = s + yy(i)
	end do
		
	s = h * (yy(1) + yy(n) + 2 * s)/ 2.0
	er = abs(s-d)
	d = s
	n = n + 1
end do

write (*,*) "Value of integration : ", s

end program integrate

subroutine f(x, y)
implicit none
real :: x, y

y = x * x		! Function to Integrate

end subroutine
