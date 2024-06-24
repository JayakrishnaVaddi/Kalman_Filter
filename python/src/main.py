import numpy as np
import matplotlib.pyplot as plt

from KFilter import KF

def main():

    plt.ion()
    plt.figure()

    kf = KF(initial_x = 0.0, initial_v= 1.5 , accel_variance= 0.1)

    DT = 0.1
    STEPS = 1000

    mean_values = []
    covarience_values = []
    for i in range(STEPS):
        mean_values.append(kf.mean)
        covarience_values.append(kf.cov)

        kf.raw_estimate(dt = DT)

    plt.subplot(2, 1, 1)
    plt.title("Position")
    plt.plot([mean[0] for mean in mean_values], 'r')

    plt.subplot(2, 1, 2)
    plt.title("Velocity")
    plt.plot([mean[1] for mean in mean_values], 'r')

    plt.show()
    plt.ginput(1)


if __name__ == "__main__":
    main()
