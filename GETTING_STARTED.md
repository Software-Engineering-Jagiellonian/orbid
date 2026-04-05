# Getting Started

## Prerequisites

- Python 3.10+
- RTL-SDR v3 + driver (librtlsdr)
- Linux (native or WSL2)
- SatNOGS DB account (optional, for API)
- Space-Track account (optional, for military TLE)

## First steps (week 1)

1. Clone the repo and install dependencies:
   ```
   git clone <repo-url>
   cd orbid
   pip install -r requirements.txt
   ```
2. Copy `config.example.yaml` to `config.yaml` and set your ground station coordinates.
3. Start with milestone M1: Predictor.
4. Issues within each milestone are numbered in suggested order.
5. Each module has a skeleton in `orbid/` with docstrings describing expected behavior.
6. Use `notebooks/` for prototyping, move working code to modules.

## Workflow

- Work through milestones sequentially (M1 -> M2 -> ... -> M6).
- Within each milestone, issues are ordered by dependency.
- Branch per issue: `git checkout -b issue-N-short-description`
- PR back to main when issue is done.

## Quick win (day 1)

Install skyfield and run a pass prediction for ISS over your location:

```
pip install skyfield
```

```python
from skyfield.api import load, wgs84

stations_url = 'https://celestrak.org/NORAD/elements/gp.php?CATNR=25544&FORMAT=tle'
satellites = load.tle_file(stations_url)
ts = load.timescale()

sat = satellites[0]
location = wgs84.latlon(50.0614, 19.9383, elevation_m=219)  # Krakow

t0 = ts.now()
t1 = ts.tt_jd(t0.tt + 1)  # next 24 hours

times, events = sat.find_events(location, t0, t1, altitude_degrees=10.0)
for t, event in zip(times, events):
    name = ('AOS', 'MAX', 'LOS')[event]
    print(f'{t.utc_strftime("%Y-%m-%d %H:%M:%S")} {name}')
```

This validates your setup and gives you a feel for the predictor module.
