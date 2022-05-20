import numpy as np
import matplotlib.pyplot as plt

def plot2D(func, xrange, filename, plot_label,ylim=None, color='black', figsize=(10, 5)):
    
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(xrange, func(xrange), color=color, label=f"${plot_label}$")
    ax.plot(xrange, func(xrange), color=color, label=f"${plot_label}$")
    ax.axhline(y=0, color='k', lw=.75)
    ax.axvline(x=0, color='k', lw=.75)

    if ylim is not None:
        ax.set_ylim(*ylim)
    
    ax.set_xlim(*xrange[[0, -1]])
    ax.set_title(f"${plot_label}$", size=25)

    fig.savefig(filename, dpi=200)
    plt.show()

def plot3Dline(func, xrange,yrange, filename, plot_label, zlim=None, color='black', figsize=(10, 5)):
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ax.plot(xrange,yrange,func(xrange,yrange))

    if zlim is not None:
        ax.set_zlim(*zlim)
    
    ax.set_xlim(*xrange[[0, -1]])
    ax.set_ylim(*yrange[[0, -1]])
    ax.set_title(f"${plot_label}$", size=25)

    fig.savefig(filename, dpi=200)
    plt.show()

def plot3Dsurf(func, xrange,yrange, filename, plot_label, zlim=None, color='black', figsize=(10, 5)):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ax.plot_surface(xrange,yrange,func(xrange,yrange))
    ax.set_title(f"${plot_label}$", size=25)
    fig.savefig(filename, dpi=200)
    plt.show()
