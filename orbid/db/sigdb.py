"""SatNOGS DB and SigIDWiki interface for transmitter signatures."""


class SignatureDB:
    """Interface to satellite transmitter databases.

    Fetches and caches transmitter metadata from SatNOGS DB API:
    frequencies, modulation types, bandwidths, baud rates.
    """

    SATNOGS_API = "https://db.satnogs.org/api/"

    def __init__(self, cache_path="data/signatures"):
        self.cache_path = cache_path

    def fetch_transmitters(self, satellite_norad_id=None):
        """Fetch transmitter records from SatNOGS DB."""
        raise NotImplementedError

    def get_signature(self, transmitter_id):
        """Get signal signature for a known transmitter."""
        raise NotImplementedError

    def search_by_frequency(self, freq_hz, tolerance_hz=5000):
        """Find transmitters matching a frequency within tolerance."""
        raise NotImplementedError
