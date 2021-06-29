import matplotlib.pyplot as plt

def SIR(r=2.3, a=1, N=100, t_0=4, t_end=30, dt=0.1, I_0=1, R_0=0):
    t = [t_0]
    S = [N-I_0]
    I = [I_0]
    R = [R_0]
    for i in range(int((t_end - t_0)/dt)):
        t.append(t[i] + dt)
        S.append(S[i] - (r * I[i] * S[i] * dt / N))
        I.append(I[i] + (I[i] * dt * ((r * S[i] / N) - a)))
        R.append(R[i] + (a * dt * I[i]))
    ax = plt.subplot()
    plt.plot(t, S, t, I, t, R)
    plt.legend(['Susceptible', 'Infected', 'Removed'])
    plt.xlabel('time')
    plt.ylabel('number of cases')
    plt.title('SIR model for epidemic modelling')
    for ar in [S,I,R]:
        ax.annotate(round(ar[-1]), xy=(t[-1],ar[-1]))
    return

SIR()
plt.tight_layout()
plt.show()
