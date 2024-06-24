import numpy as np
import matplotlib.pyplot as plt

class KF:
    def __init__(self, initial_x: float, 
                       initial_v: float,
                       accel_variance: float) -> None:
        
        #mean of state
        self.x = np.array([initial_x, initial_v])
        self.accel_variance = accel_variance

        #covarience of the state
        self.P = np.eye(2)

    def raw_estimate(self, dt: float) -> None: 

        # x = F x
        # P = F P Ft  + G a Gt

        F = np.array([[1, dt],[0, 1]])
        G = np.array([(1/2)*dt*dt , dt]).reshape((2, 1))

        x_new = F.dot(self.x)
        p_new = F.dot(self.P).dot(F.T) + G.dot(G.T)* self.accel_variance

        self.x = x_new
        self.P = p_new

    def update_estimates(self, meas_value:float, meas_variance: float) -> None:

        # Y = Zh - H Xh
        # Sh = H Pk Ht + R
        # K = Ph Ht Sk.inv
        # X_z = Xh + K.Y
        # P_z = (I - K H). Ph

        H = np.array([1, 0]).reshape((1, 2))

        Zh = np.array([meas_value])
        R = np.array([meas_variance])

        Y = Zh - H.dot(self.x)
        Sh = H.dot(self.P).dot(H.T) + R 
        K = self.P.dot(H.T).dot(np.linalg.inv(Sh))

        new_x = self.x + K.dot(Y)
        new_p = np.eye(2) - K.dot(H).dot(self.P)

        self.x = new_x
        self.P = new_p


    @property
    def cov(self):
        return self.P
    
    @property
    def mean(self):
        return self.x

    @property
    def position(self) -> float:
        return self.x[0]
    
    @property
    def velocity(self) -> float:
        return self.x[1]

