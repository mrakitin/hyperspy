import os
from hyperspy.api import load

my_path = os.path.dirname(__file__)


class TestFindPeaks1DOhaver():

    def setup_method(self, method):
        self.signal = load(
            my_path +
            "/test_find_peaks1D_ohaver/test_find_peaks1D_ohaver.hdf5")

    def test_find_peaks1D_ohaver_high_amp_thres(self):
        signal1D = self.signal
        peak_list = signal1D.find_peaks1D_ohaver(amp_thresh=10.)[0]
        assert len(peak_list) == 0

    def test_find_peaks1D_ohaver_zero_value_bug(self):
        signal1D = self.signal
        peak_list = signal1D.find_peaks1D_ohaver()[0]
        assert len(peak_list) == 48
