# orbid

Automated LEO satellite signal detection and attribution framework using software-defined radio.

## Overview

orbid is a Python framework that correlates orbital predictions with RF signal detection to attribute observed satellite transmissions to specific objects in orbit. It uses an RTL-SDR receiver to scan VHF/UHF/L-band frequencies during predicted satellite passes and classifies detected signals against a database of known satellite transmitter signatures.

## Architecture

```
predictor ──▶ scanner ──▶ detector ──▶ classifier ──▶ correlator
 (TLE/SGP4)   (RTL-SDR)   (DSP/FFT)   (sigprint)     (report)
```

**predictor** generates pass schedules for satellites over a given ground station using TLE data and SGP4 propagation. Filters satellites by operator, COSPAR designator, or orbital group.

**scanner** controls the RTL-SDR hardware. Operates in two modes: wideband survey (power spectral density sweep) and targeted recording (IQ capture during predicted pass windows).

**detector** performs spectral analysis on recorded data. Estimates noise floor, detects signals above an adaptive SNR threshold, and extracts signal parameters: center frequency, occupied bandwidth, Doppler drift.

**classifier** compares detected signal features against a reference database of known satellite transmitter signatures (modulation type, symbol rate, bandwidth). Reference data sourced from SatNOGS DB and SigIDWiki.

**correlator** fuses RF detections with orbital predictions. Evaluates temporal overlap (detection within AOS/LOS window), frequency match (accounting for Doppler shift), and signature match. Produces an attribution report with a multi-factor confidence score.

## Target frequency bands

| Band | Range | Signals |
|------|-------|---------|
| VHF | 136-138 MHz | APT/LRPT weather satellites (NOAA, Meteor-M) |
| VHF | 144-146 MHz | Amateur LEO satellites |
| UHF | 400-403 MHz | LEO telemetry |
| UHF | 435-438 MHz | Amateur LEO, CubeSats |
| L-band | 1598-1616 MHz | GLONASS L1 (FDMA) |

## Installation

```bash
git clone https://github.com/Software-Engineering-Jagiellonian/orbid.git
cd orbid
pip install -r requirements.txt
```

Copy `config.example.yaml` to `config.yaml` and set your ground station coordinates and SDR parameters.

## Hardware

- RTL-SDR v3 (or compatible receiver)
- Antenna: wideband discone, or dedicated VHF turnstile/QFH + L-band patch
- Optional: LNA (e.g. Nooelec SAWbird for 137 MHz or L-band)
- Linux host (native or WSL2)

## Data sources

- [CelesTrak](https://celestrak.org) / [Space-Track](https://space-track.org) for TLE orbital elements
- [SatNOGS DB](https://db.satnogs.org) for satellite transmitter database and community observations
- [SigIDWiki](https://sigidwiki.com) for signal identification reference
- [UCS Satellite Database](https://ucsusa.org/resources/satellite-database) for operator/country metadata

## Recording format

IQ recordings use the [SigMF](https://sigmf.org) metadata standard for interoperability with GNU Radio and the SatNOGS ecosystem.

## License

See [LICENSE](LICENSE).
