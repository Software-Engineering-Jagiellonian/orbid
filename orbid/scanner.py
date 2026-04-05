"""RTL-SDR control for wideband survey and targeted IQ recording."""


class Scanner:
    """Controls RTL-SDR hardware for signal acquisition.

    Two operating modes:
    - survey: wideband power spectral density sweep
    - targeted: IQ recording during predicted pass windows
    """

    def __init__(self, config):
        self.config = config

    def connect(self, device_index=0):
        """Initialize RTL-SDR device."""
        raise NotImplementedError

    def survey(self, freq_start, freq_end, bin_size=1000):
        """Sweep frequency range and record power spectral density."""
        raise NotImplementedError

    def record_pass(self, center_freq, sample_rate, duration, output_path):
        """Record IQ data for a satellite pass window.

        Saves in SigMF format (raw IQ + JSON metadata).
        """
        raise NotImplementedError
