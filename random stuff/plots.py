import matplotlib.pyplot as plt
import numpy as np

def make_plots(rawdata, dmd_recon, pos_recon, pos_evals, dmd_evals, lbl):
    fig = plt.figure()

    #plot cm_data with recon
    ax = fig.add_subplot(131)
    ax.plot(rawdata[0,0,:], rawdata[0,1,:],linewidth=2,linestyle='-',color='k',label='RK4')
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    ax.legend()
    ax = fig.add_subplot(132)
    ax.plot(dmd_recon[0,:], dmd_recon[1,:],linewidth=2,linestyle='-', color='b',label='DMD')
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    ax.legend()
    ax = fig.add_subplot(133)
    ax.plot(pos_recon[0,0,:], pos_recon[0,1,:],linewidth=2,linestyle='-', color='r',label='Pos_DMD')
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    ax.legend()
    fig.tight_layout()

    fig.savefig("dmd_test_" + lbl, dpi=200)

    #Eigenvalues
    fig = plt.figure()
    ax = fig.add_subplot(111)
    t = np.linspace(0, 2*np.pi, 300)
    ax.plot(np.cos(t), np.sin(t), linewidth=1)
    ax.scatter(np.real(dmd_evals), np.imag(dmd_evals),alpha = 0.25,label='DMD $\lambda$s')
    ax.scatter(np.real(pos_evals), np.imag(pos_evals),alpha = 0.25,label='Pos DMD $\lambda$s')
    ax.set_xlabel("Real $(\lambda)$")
    ax.set_ylabel("Imag $(\lambda)$")
    ax.set_title("Eigenvalues")
    ax.legend()
    fig.tight_layout()
    fig.savefig("dmd_test_eig_"+lbl, dpi=200)