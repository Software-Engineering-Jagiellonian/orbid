"""Signal classification against known satellite transmitter signatures."""


class SignalClassifier:
    """Matches detected signals to known transmitter signatures.

    Compares extracted features (modulation, bandwidth, symbol rate)
    against the signature database sourced from SatNOGS DB and SigIDWiki.
    """

    def __init__(self, config):
        self.config = config

    def load_signatures(self, db_path=None):
        """Load transmitter signature database."""
        raise NotImplementedError

    def classify(self, detection):
        """Match a detection against known signatures.

        Returns ranked list of (transmitter_id, similarity_score) tuples.
        """
        raise NotImplementedError
