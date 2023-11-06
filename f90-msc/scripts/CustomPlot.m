# 

set si sq
set title("")
set xlabel("")
set ylabel("")
set xrange[:]
set yrange[:]
set grid
plot "abc.txt" w lp pt # ps # lw # lc # t "abc", "pqr.txt" w lp pt # ps # lw # lc # t "pqr"

set term png
set output "123.png"
replot
