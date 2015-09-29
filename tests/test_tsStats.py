#Must include the above directory in the path
import sys, os
root_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
sys.path.append(root_dir)

# The testing module must be imported in all tests
import pytest
import numpy as np

# Test specific includes begin here
import tsStats

class TesttsStats:
    def test_CO_AutoCorr(self):
        y = np.array([12,24,15,23,17,10,8,9,24,11,13,24,41,52,12,2,5,14,16,25,34])
        tau = 1
        assert abs(tsStats.CO_AutoCorr(y,tau) -  0.4015) < 0.0001
