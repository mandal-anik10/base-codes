! #12 Defining Function : Volume of a Cylinder
! NAME : ANIK MANDAL - 21024001
! DATE : MAR 29, 2022
!__________________________________________________

program func
implicit none
real :: Vol_Cy, r, h, v

write(*,*) "Give radius and height of the Cylinder"
read(*,*) r, h

v = Vol_Cy(r, h)

write(*,*) "Volume of the Cylinder ", v

end program func


function Vol_Cy(radius, height)
implicit none
real :: radius, height, Vol_Cy


Vol_Cy =  4.0 * ATAN(1.0) * (radius**2) * height


end function Vol_Cy