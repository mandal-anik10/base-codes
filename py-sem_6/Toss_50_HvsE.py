
import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(2, 1)

event_n = 1000
toss_n = 100

count = []
avg_c = []
event = [i for i in range(event_n)]

for i in range(len(event)):
    toss = np.random.randint(0, 2, size=toss_n)         # 0 as tail and 1 as head
    c = 0
    for j in range(toss_n):
        if toss[j] == 1:
            c = c+1
    count.append(c)
    d = 0
    for j in range(len(count)):
        d = d + count[j]
    avg_c.append(d/len(count))

ax1.plot(event, count)
ax1.set_ylabel('Head_n')

ax2.plot(event, avg_c)
ax2.set_xlabel('Event_n')
ax2.set_ylabel('Avg. Head_n')
ax2.set_title('Final Avg number of Head: '+str(avg_c[event_n-1]))

fig.suptitle('Number of events: '+str(event_n)+', Number of toss per event: '+str(toss_n))

plt.show()
