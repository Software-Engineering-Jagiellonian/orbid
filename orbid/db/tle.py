"""TLE fetch, parse, and cache."""


class TLEStore:
    """Manages TLE data from CelesTrak and Space-Track.

    Handles fetching, parsing, local caching with staleness checks,
    and filtering by satellite group or catalog properties.
    """

    def __init__(self, cache_dir="data/tle"):
        self.cache_dir = cache_dir

    def fetch_celestrak(self, group="active"):
        """Fetch TLE set from CelesTrak by group name."""
        raise NotImplementedError

    def fetch_spacetrack(self, norad_ids):
        """Fetch TLE set from Space-Track by NORAD IDs."""
        raise NotImplementedError

    def get_tle(self, norad_id):
        """Get cached TLE for a specific satellite."""
        raise NotImplementedError
