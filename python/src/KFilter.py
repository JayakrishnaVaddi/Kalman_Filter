import numpy as np

class KF:
    def __init__(self, initial_x: float, 
                       initial_v: float,
                       accelVariance: float) -> None:
        
        #mean of state
        self.state_values = np.array([initial_x, initial_v])
        self.accelVariance = accelVariance

        #covarience of the state
        self.covariences = np.eye(2)

    def raw_estimate(self, dt: float) -> None: 

        # x = F x
        # P = F P Ft  + G a Gt

        F = np.array([[1, dt],[0, 1]])
        G = np.array([(1/2)*dt*dt , dt]).reshape((2, 1))

        x_new = F.dot(self.state_values)
        p_new = F.dot(self.covariences).dot(F.T) + G.dot(G.T)* self.accelVariance

        self.state_values = x_new
        self.covariences = p_new

    def update_estimates(self, meas_position:float, meas_variance: float) -> None:

        # Y = Zh - H Xh
        # Sh = H Pk Ht + R
        # K = Ph Ht Sk.inv
        # X_z = Xh + K.Y
        # P_z = (I - K H). Ph

        H = np.array([1, 0]).reshape((1, 2))

        Zh = np.array([meas_position])
        R = np.array([meas_variance])

        Y = Zh - H.dot(self.state_values)
        Sh = H.dot(self.covariences).dot(H.T) + R 
        K = self.covariences.dot(H.T).dot(np.linalg.inv(Sh))

        new_x = self.state_values + K.dot(Y)
        new_p = (np.eye(2) - K.dot(H)).dot(self.covariences)

        self.state_values = new_x
        self.covariences = new_p


    @property
    def cov(self):
        return self.covariences
    
    @property
    def mean(self):
        return self.state_values

    @property
    def position(self) -> float:
        return self.state_values[0]
    
    @property
    def velocity(self) -> float:
        return self.state_values[1]

