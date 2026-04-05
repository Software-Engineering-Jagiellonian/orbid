"""Attribution engine: correlate RF detections with orbital predictions."""


class Correlator:
    """Fuses signal detections with pass predictions for attribution.

    Evaluates three correlation axes:
    - temporal: detection timestamp within AOS/LOS window
    - spectral: detection frequency matches known downlink +/- Doppler
    - signature: detected signal features match transmitter profile

    Produces attribution report with multi-factor confidence score.
    """

    def __init__(self, config):
        self.config = config

    def correlate(self, detections, passes):
        """Run correlation pipeline.

        Returns list of Attribution objects with satellite ID,
        detection reference, correlation factors, and confidence.
        """
        raise NotImplementedError

    def validate_doppler(self, observed_drift, predicted_drift):
        """Compare observed Doppler drift against SGP4 prediction."""
        raise NotImplementedError
