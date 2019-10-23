import numpy as np
import matplotlib.pyplot as plt


def heterogenetic_pop(n, l, gf):
    return np.array([
        np.array([
            gf() for i in range(l)
        ]) for j in range(n)
    ])


def ez_plot(ret):    
    fig, ax1 = plt.subplots()
    ax1.set_title("Gen Alg")
    ax1.set_xlabel('Generation')
    ax1.set_ylabel('Score')
    ax1.plot(ret[:, 0], c='r', label='Max Score')
    ax1.plot(ret[:, 1], c='b', label='Average Score')
    ax1.plot(ret[:, 2], c='g', label='Min Score')
    ax1.legend()
    plt.show()