import matplotlib.pyplot as plt

def SVIRD(r=2.3, a=1, v=1, d=0.3, N=100, t_0=4, t_end=40, dt=0.1, I_0=1, R_0=0, V_0 = 0, D_0=0):
    t = [t_0]
    S = [N-I_0]
    V = [V_0]
    I = [I_0]
    R = [R_0]
    D = [D_0]
    for i in range(int((t_end - t_0)/dt)):
        if round(S[i]) == 0:
            v = 0
        t.append(t[i] + dt)
        S.append(S[i] - (r * I[i] * S[i] * dt / N) - (v * dt))
        V.append(V[i] + (v * dt))
        I.append(I[i] + (I[i] * dt * ((r * S[i] / N) - a)) - (d * dt * I[i]))
        R.append(R[i] + (a * dt * I[i]))
        D.append(D[i] + (d * dt * I[i]))
    ax = plt.subplot()
    plt.plot(t, S, t, V, t, I, t, R, t, D)
    plt.legend(['Susceptible', 'Vaccinated', 'Infected', 'Recovered', 'Dead'])
    plt.xlabel('time')
    plt.ylabel('number of cases')
    plt.title('Extended SIR model with vaccination and death')
    for ar in [S, V, I, R, D]:
        ax.annotate(round(ar[-1]), xy=(t[-1],ar[-1]))
    return

SVIRD()
plt.tight_layout()
plt.show()