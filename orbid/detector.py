"""Signal detection via spectral analysis."""


class SignalDetector:
    """Detects satellite signals above noise floor in IQ recordings.

    Performs FFT-based spectral analysis, estimates noise floor,
    and extracts signal parameters for each detection.
    """

    def __init__(self, config):
        self.config = config

    def analyze(self, iq_path):
        """Run detection pipeline on an IQ recording.

        Returns list of Detection objects with:
        - center frequency
        - occupied bandwidth
        - SNR estimate
        - Doppler drift rate
        - time span within recording
        """
        raise NotImplementedError

    def estimate_noise_floor(self, spectrum):
        """Adaptive noise floor estimation using median or CFAR."""
        raise NotImplementedError
