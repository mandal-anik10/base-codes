! #2 FINDING LARGEST OUT OF 4 NUMBERS
! NAME : ANIK MANDAL - 21024001
! DATE : Fed 24, 2022
!__________________________________________________

program loop
implicit none
integer:: a, b, c, d, big

write(*,*) "Provide four integers"
read(*,*) a, b, c, d
write(*,*) "a=", a, "b=", b, "c=", c, "d=", d

big = a

if (b > big) then 
	big = b
end if

if (c > big) then
	big = c
end if

if (d > big) then
	big = d
end if

write(*,*) "Largest integer is", big

end program loop
