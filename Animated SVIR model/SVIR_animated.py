import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation




# parameters to vary:
r_max = 0.5
r_min = 2
r_step = 100
a = 1  # recovery rate
v = 2 # vaccination rate

# initial conditions:
t_0 = 0
t_end = 30
dt = 0.1  # step size
N = 100  # population size
S_0 = N - 1
I_0 = 1
R_0 = 0
V_0 = 0

fig, (ax, ax2) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]})
fig.suptitle('Flattening the curve: SIR model for varying r/a')
plotS, = ax.plot([], [], 'b')
plotV, = ax.plot([], [], 'g')
plotI, = ax.plot([], [], 'r')
plotR, = ax.plot([], [], 'k')
ax.set(title='--.-% were infected')
ax.legend(['Susceptible', 'Vaccinated', 'Infected', 'Removed'], loc='right')
ax.set_xlim(t_0, t_end)
ax.set_ylim(0, N)
ax.set(xlabel='time', ylabel='% of individuals')
# ax2.axes.yaxis.set_visible(False)


ax2.set_ylim(0,2)
ax2.set_xlim(0,r_min)

plotaline, = ax2.plot([0, r_min], [0.5, 0.5], 'g')
plotrline = ax2.plot([0, r_min], [1, 1], 'b')
plotvline = ax2.plot([0, r_min], [1.5, 1.5], 'y')
# plota = ax2.plot([], [], 'o')
plotr, = plt.plot(r_min, 1, 'bo')
plota, = plt.plot(a, 0.5, 'go')
plotv, = plt.plot(v, 1.5, 'yo')

ax2.set_title(f'r/a={r_min/a}')
ax2.set_yticks([0.5, 1, 1.5])
ax2.set_yticklabels(['a','r', 'v'])


def update(frame):
    t = [t_0]
    S = [S_0]
    I = [I_0]
    R = [R_0]
    V = [V_0]
    for i in range(int(t_end/dt)):
        t.append(t[i] + dt)
        S.append(S[i] - (frame * I[i] * S[i] * dt / N) - (dt * v * S[i] / N))
        I.append(I[i] + (I[i] * dt * ((frame * S[i] / N) - a)))
        R.append(R[i] + (a * dt * I[i]))
        V.append(V[i] + (dt * v * S[i] / N))
    # print(frame)
    tt = next((int(round(i*dt,0)) for i, x in enumerate(I) if round(x,1) == 0.0), None)
    # days = ''
    if tt:
        days = f'the pandemic took {tt} timepoints'
    else:
        days = f'took >{t_end} days'
    ax.set(title=(f'{round(R[-1],1)}% were infected, '+days))
    plotS.set_data(t, S)
    plotI.set_data(t, I)
    plotR.set_data(t, R)
    plotV.set_data(t, V)
    plotr.set_data(frame, 1)
    ax2.set_yticklabels([f'a={a}', f'r={round(frame,1)}', f'v={v}'])
    ax2.set_title(f'r / a = {round(frame/a,1)}')
    return plotS, plotI, plotR, plotV, plotr

# update(1)
ani = FuncAnimation(fig, update, frames=np.linspace(r_min, r_max, r_step), blit=False, interval=150)
plt.tight_layout()
plt.show()

ani.save('SVIR_animated.gif')

