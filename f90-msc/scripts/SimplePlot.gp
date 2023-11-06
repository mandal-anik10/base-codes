# #A SIMPLE PLOT
# NAME : ANIK MANDAL - 21024001
# DATE : Apr 25, 2022
#__________________________________________________

plot "VvsI.txt" u 1:2
set terminal png size 1600,1600
set output "SimplePlot.png"
replot

