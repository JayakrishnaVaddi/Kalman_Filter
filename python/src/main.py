import numpy as np
import matplotlib.pyplot as plt

from KFilter import KF

def main():

    plt.ion()
    plt.figure()

    x_real = 0.0
    v_real = 0.9
    meas_varience = 0.01

    kf = KF(initial_x = 0.0, initial_v= 2.5 , accelVariance= 0.01)

    DT = 0.1
    STEPS = 1000
    MEASUREMENT_STEPS = 20

    mean_values = []
    covarience_values = []
    for step in range(STEPS):
        mean_values.append(kf.mean)
        covarience_values.append(kf.cov)

        x_real = x_real+DT*v_real
        kf.raw_estimate(dt = DT)
        if step != 0 and step % MEASUREMENT_STEPS == 0:
            kf.update_estimates(meas_position=x_real+np.random.randn()* np.sqrt(meas_varience), meas_variance=meas_varience)

    plt.subplot(2, 1, 1)
    plt.title("Position")
    plt.plot([mean[0] for mean in mean_values], 'r')
    plt.plot([mean[0] + 2*np.sqrt(covarience[0,0]) for mean, covarience in zip(mean_values, covarience_values)], '--r')
    plt.plot([mean[0] - 2*np.sqrt(covarience[0,0]) for mean, covarience in zip(mean_values, covarience_values)], '--r')

    plt.subplot(2, 1, 2)
    plt.title("Velocity")
    plt.plot([mean[1] for mean in mean_values], 'r')
    plt.plot([mean[1] + 2*np.sqrt(covarience[1,1]) for mean, covarience in zip(mean_values, covarience_values)], '--r')
    plt.plot([mean[1] - 2*np.sqrt(covarience[1,1]) for mean, covarience in zip(mean_values, covarience_values)], '--r')


    plt.show()
    plt.ginput(1)


if __name__ == "__main__":
    main()
