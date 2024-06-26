from KFilter import KF

import numpy as np
import unittest

class Test_KFilter(unittest.TestCase):
    def test_initialization(self):

        x = 0.3
        v = 0.5
        a_v = 1.2
        kf = KF(initial_x= x, initial_v=v, accelVariance=a_v)

        self.assertAlmostEqual(x, kf.position)
        self.assertAlmostEqual(v , kf.velocity)

    def test_can_predict(self):
        
        x = 0.3
        v = 0.5
        a_v = 1.2
        kf = KF(initial_x= x, initial_v=v, accelVariance=a_v)
        kf.raw_estimate(dt = 0.1)

    def test_raw_estimate_matrix_shape(self):

        x = 0.3
        v = 0.5
        a_v = 1.2
        kf = KF(initial_x= x, initial_v=v, accelVariance=a_v)

        self.assertEqual(kf.cov.shape, (2, 2))
        self.assertEqual(kf.mean.shape, (2, ))

    def test_uncertainity_increase(self):

        x = 0.3
        v = 2.5
        a_v = 1.2
        kf = KF(initial_x= x, initial_v=v, accelVariance=a_v)


        for i in range(10):
            det_before = np.linalg.det(kf.cov)
            kf.raw_estimate(dt = 0.1)
            det_after = np.linalg.det(kf.cov)

            self.assertGreater(det_after, det_before)

    def test_updating_estimates(self):

        x = 0.3
        v = 0.5
        a_v = 1.2

        kf = KF(initial_x= x, initial_v=v, accelVariance=a_v)

        kf.raw_estimate(dt = 0.1)
        kf.update_estimates(meas_position=0.1 , meas_variance=0.1)

    def test_state_decrease_uncertainingy(self):

        x = 0.3
        v = 2.5
        a_v = 1.2

        kf = KF(initial_x= x, initial_v=v, accelVariance=a_v)


        det_before = np.linalg.det(kf.cov)
        kf.update_estimates(meas_position=0.1 , meas_variance=0.01)
        det_after = np.linalg.det(kf.cov)
        
        self.assertLess(det_after, det_before)

    def test_matrix_shapes_after_update(self):

        x = 0.3
        v = 2.5
        a_v = 1.2

        kf = KF(initial_x= x, initial_v=v, accelVariance=a_v)
        kf.update_estimates(meas_position=0.1 , meas_variance=0.01)

        self.assertEqual(kf.cov.shape , (2, 2))
        self.assertEqual(kf.mean.shape, (2, ))